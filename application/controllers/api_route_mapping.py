# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================


from application import app
from flask import render_template
from application.models.greet import Greet

@app.route('/')
def start():
    return render_template('index.html', message = "")

@app.route('/greet')
def greet():
    _greet = Greet()
    return render_template('index.html', message=_greet.show_string())

