#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =======================================
# Auther : NareN
# git    : https://github.com/DEVELByte
# =======================================
import os
import re

from application import app

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))


if __name__ == '__main__':
    purge(".", "nohup.out")
    app.run()
