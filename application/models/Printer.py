# -*- coding: utf-8 -*-

#=======================================
# Auther : NareN
# git    : https://github.com/DEVELByte
#=======================================

from flask import flash


class Printer(object):

    def show_string(self, text):
        if text == '':
            flash("You didn't enter any text to flash")
        else:
            flash(text + "!!!")
