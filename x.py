from flask import Flask
app = Flask(__name__)

@app.route('/')
def x():
    return "yessssirrrrrrrrrr!"

if __name__ == "__main__":
    app.run(debug=True)
import requests
requests.get()