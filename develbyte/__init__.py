# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================
import logging

from develbyte.utils.logging import Logging

__version__ = '0.1'
from flask import Flask
from dynaconf import FlaskDynaconf

from develbyte.controllers.api_route_mapping import greet_app
from develbyte.errors import app_error_handler

logger = logging.getLogger("default")


def create_app(config_name=None):
    app = Flask(__name__)
    if not config_name:
        config_name = "./settings/settings.development.yml," \
                      "./settings/settings.testing.yml," \
                      "./settings/settings.production.yml"
    FlaskDynaconf(app, SETTINGS_MODULE_FOR_DYNACONF=config_name)
    Logging().init_app(app)
    app.register_blueprint(greet_app)
    app.register_blueprint(app_error_handler)
    logger.info("Flask App Created")

    return app

