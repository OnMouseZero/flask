#coding=utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World! this is v11.0.1版本的flask"
=======
    return "Hello World! this is v14.0版本的flask"
>>>>>>> 44fe6e28fc5d9ce26d211cab966b3f64ad0ee833

if __name__ == "__main__":
    app.run(host='0.0.0.0')
