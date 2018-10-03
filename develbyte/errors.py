# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================

"""Application error handlers."""
from flask import jsonify, Blueprint

app_error_handler = Blueprint('errors', "app_error_handlers")


@app_error_handler.app_errorhandler(404)
def page_not_found(e):
    return jsonify({"code": "404", "message": "Resource Not Found", "exception": str(e)})
