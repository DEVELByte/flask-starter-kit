# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================
import logging
from flask import Blueprint, jsonify, current_app
from develbyte.models.greet import Greet


greet_app = Blueprint('greet', __name__, url_prefix='/develbyte')
logger = logging.getLogger("default")


@greet_app.route('/greet')
def greet():
    logger.info("getting the greet message from model")
    _greet = Greet()
    return jsonify({"message": _greet.show_string()})
