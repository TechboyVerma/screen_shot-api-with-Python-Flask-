Demo:
![screenshot (5)](https://github.com/TechboyVerma/screen_shot-api-with-Python-Flask-/assets/114131682/fecbe675-0729-4af6-bc36-e2c6e87777b1)
![screenshot (4)](https://github.com/TechboyVerma/screen_shot-api-with-Python-Flask-/assets/114131682/e4d22581-a90f-45da-985c-02d140548f06)
![screenshot (6)](https://github.com/TechboyVerma/screen_shot-api-with-Python-Flask-/assets/114131682/0d91e4f8-0912-40ca-a93f-c51ac015381b)


Python ke through screenshot API create karna ek kaafi useful project hai, jo alag-alag applications mein use ho sakta hai, jaise ke monitoring tools, bug reporting systems, aur remote assistance. Chaliye dekhte hain kaise aap Python mein screenshot API bana sakte hain:

### Step-by-Step Guide to Create a Screenshot API in Python

#### Requirements:
1. **Python**: Make sure you have Python installed on your system.
2. **Flask**: For creating the web API.
3. **Pillow**: For image processing.
4. **PyAutoGUI**: For taking screenshots.

#### Installation:
Pehle, aapko kuch libraries install karni hongi. Ye commands use karke libraries install kar sakte hain:

```bash
pip install Flask Pillow pyautogui
```

#### Code:
Ek simple Flask application banate hain jo screenshot le aur usse save karke return kare:

```python
from flask import Flask, send_file
from datetime import datetime
import pyautogui
import os

app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def take_screenshot():
    # Screenshot ka naam aur path set karte hain
    screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot_path = os.path.join("screenshots", screenshot_name)

    # Screenshot le kar save karte hain
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    # Screenshot file ko response mein bhejte hain
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    app.run(debug=True)
```

#### Explanation:
1. **Importing Libraries**:
   - `Flask` se API banate hain.
   - `datetime` se current timestamp le kar unique screenshot naam generate karte hain.
   - `pyautogui` se screenshot lete hain.
   - `os` se file paths handle karte hain.

2. **Setting Up Flask App**:
   - Ek Flask app create karte hain aur ek route define karte hain `/screenshot`, jo GET request handle karega.

3. **Taking Screenshot**:
   - `pyautogui.screenshot()` function use karke screenshot lete hain.
   - Screenshot ko `screenshots` folder mein save karte hain, jo agar exist nahi karta to pehle create kar lete hain.

4. **Returning Screenshot**:
   - `send_file` function use karke screenshot ko response mein bhejte hain, taaki client usse download kar sake.

#### Running the API:
API run karne ke liye, aap terminal mein ye command use kar sakte hain:

```bash
python app.py
```

API successfully run hone par, aap browser mein `http://127.0.0.1:5000/screenshot` URL ko hit karke screenshot le sakte hain.

Is tarah se aap ek simple aur effective screenshot API create kar sakte hain Python aur Flask ka use karke. Ye API aapke projects mein asani se integrate ho sakti hai.
