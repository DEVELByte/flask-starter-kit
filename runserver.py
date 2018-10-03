#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================
import logging
import os
import re
import argparse
from develbyte import create_app

logger = logging.getLogger("default")


def purge(directory, pattern):
    for f in os.listdir(directory):
        if re.search(pattern, f):
            os.remove(os.path.join(directory, f))


def arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--configName', '-c', help='pass a absolute path to the config file')
    return parser.parse_args()


def print_config(config):
    for _config in config.keys():
        logger.info("{key: <50}: {value}".format(key=_config, value=config[_config]))


if __name__ == '__main__':
    purge(".", "nohup.out")
    args = arguments()
    app = create_app(args.configName)
    print_config(app.config)
    app.run(port=app.config.PORT, threaded=True)
