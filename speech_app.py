from flask import Flask, send_file
from recognizer import recognize_speech

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("page.html")

@app.route("/page_style.css")
def style():
    return send_file("page_style.css")

@app.route("/page_script.js")
def script():
    return send_file("page_script.js")

@app.route("/recognize")
def recognize():   
    text = recognize_speech()
    return text

if __name__ == "__main__":
    app.run(port=5005, debug=True)