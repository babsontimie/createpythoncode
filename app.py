# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Azure Web App!"

if __name__ == '__main__':
    app.run()
