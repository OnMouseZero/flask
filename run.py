#coding=utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! this is v2.4版本的flask"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
