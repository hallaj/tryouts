#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from .models import db


def setup(**config):
    app = Flask(__name__)
    app.config.update(**config)

    app.db = db
    app.db.init_app(app)

    return app
