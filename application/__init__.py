# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================
__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from app_config import APPLICATION_NAME, SECRET_KEY, DEBUG_MODE, TEMPLATE_PATH, STATIC_PATH

app = Flask(APPLICATION_NAME, template_folder=TEMPLATE_PATH,
            static_folder=STATIC_PATH)
app.config['SECRET_KEY'] = SECRET_KEY
app.debug = DEBUG_MODE
toolbar = DebugToolbarExtension(app)

from application.controllers import *
