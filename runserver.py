#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =======================================
# Author : NareN
# git    : https://github.com/DEVELByte
# =======================================

import os
from application import app
from app_config import PORT, IP

if __name__ == '__main__':
    port = int(os.environ.get("PORT", PORT))
    app.run(IP, port=port)
