#
# -*- coding: utf-8 -*-
# pylint: disable=W0611,C0301
# @author Vangelis Banos
"""Code to run the web server"""
from main import App
from etc import settings

if __name__ == '__main__':
    App.run(port=settings.PORT, debug=settings.DEBUG)
