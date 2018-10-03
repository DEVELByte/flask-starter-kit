# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================
import logging
import logging.config


class Logging(object):
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": None
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "default",
                "stream": "ext://sys.stdout"
            },

            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "default",
                "filename": None,
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
        },

        "loggers": {
            "default": {
                "level": "DEBUG",
                "handlers": ["console", "file"],
                "propagate": False
            }
        },

        "root": {
            "level": "DEBUG",
            "handlers": ["console", "file"]
        }
    }

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.configure_logger()

    def configure_logger(self, name='default'):
        if self.validate_settings():
            # setup the formatter
            self.config["formatters"]["default"]["format"] = self.app.config.get(
                'LOG_FORMATTER',
                '[%(asctime)s] %(levelname)s in %(filename)s:%(lineno)d - %(message)s'
            )

            # setup Log level
            self.config["loggers"]["default"]["level"] = self.app.config.get('LOG_LEVEL', 'DEBUG')

            # Log file handler
            # self.config["handlers"]["file"]["filename"] = self.app.config.get('LOGGING_FILE_HANDLER',
            #                                                                   'logging.handlers.RotatingFileHandler')

            # setup Log file name
            _log_path = self.app.config.get('LOG_PATH', './logs/')
            _log_file_name = "{}.log".format(self.app.config.get('LOG_FILE_NAME', 'application'))
            self.config["handlers"]["file"]["filename"] = '{}{}'.format(_log_path, _log_file_name)

            if name not in self.config["loggers"]:
                self.config["loggers"][name] = self.config["loggers"]["default"]

            logging.config.dictConfig(self.config)

        return logging.getLogger(name)

    def validate_settings(self):
        _config_log_level = self.app.config.get('LOG_LEVEL', 'DEBUG')
        if _config_log_level:
            config_log_int = getattr(logging, _config_log_level.upper(), None)
            if not isinstance(config_log_int, int):
                raise ValueError(
                    'Invalid log level: {0}'.format(_config_log_level)
                )
            else:
                return True
