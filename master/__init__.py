#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


def setup(**config):
    app = Flask(__name__)
    app.config.update(**config)

    return app
