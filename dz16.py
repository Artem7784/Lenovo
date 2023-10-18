from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/main')
def main():
    return '<p>main</p>'

@app.route('/one')
def one():
    return '<p>one</p>'

@app.route('/two')
def two():
    return '<p>two</p>'

app.run()