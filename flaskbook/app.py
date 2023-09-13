from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, flaskbook!'

def test(a: int, b, c):
    a += 10
    return 'test'