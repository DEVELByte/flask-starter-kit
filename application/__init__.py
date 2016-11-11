# -*- coding: utf-8 -*-

#=======================================
# Auther : NareN
# git    : https://github.com/DEVELByte
#=======================================

__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
app = Flask('application')
app.config['SECRET_KEY'] = 'develbyte'
app.debug = True
toolbar = DebugToolbarExtension(app)
from application.controllers import *
