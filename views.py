from settings import *
from flask import render_template


@app.route('/')
def hello_world():
    a = 1
    return 'Hello World'
