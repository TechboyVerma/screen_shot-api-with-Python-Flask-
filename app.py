from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, storage, db, firestore
import pyautogui

import io

import datetime

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('screenshotapikey.json') #yours database api keys
firebase_admin.initialize_app(cred, {
    'storageBucket': 'human-resourse-managemen-cc065.appspot.com',
    'databaseURL': 'https://human-resourse-managemen-cc065-default-rtdb.firebaseio.com'
})
bucket = storage.bucket()

# Route to accept screenshot data
@app.route('/upload-screenshot', methods=['POST'])
def upload_screenshot():

    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to a byte buffer as JPG
    byte_buffer = io.BytesIO()
    screenshot.save(byte_buffer, format='JPEG')  # Save as JPEG
    screenshot_bytes = byte_buffer.getvalue()

    # Get user UID from request
    user_uid = request.json.get('user_uid')

    # Store screenshot in Firebase Storage
    blob = bucket.blob(
        'screenshots/Employee/{}/screenshot.jpg'.format(user_uid))
    blob.upload_from_string(screenshot_bytes, content_type='image/jpeg')

    # Get download URL of the uploaded screenshot
    download_url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 15 minutes
        expiration=datetime.timedelta(minutes=60),
        method='GET',
        response_disposition='attachment; filename=screenshot.jpg'  # Specify the filename
    )  # URL expires in 1 hour

    # Save download URL in Firestore under the path "/Employee/{user_uid}/screenshot"
    db = firestore.client()  # Initialize Firestore client
    screenshot_doc_ref = db.collection('Employee').document(
        user_uid).collection('screenshot').document("ss")
    screenshot_doc_ref.set({
        'download_url': download_url
    })

    return f'Screenshot uploaded successfully: {download_url}'

if __name__ == '__main__':
    # Specify the port you want to use, for example, 8080
    port = 3000
    # Start the Flask app with the specified port
    app.run(host='0.0.0.0', port=port)
