#! /home/song/web-course/flasky/venv/bin/python3
print('worked')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
