#!/usr/bin/env python
# -*- coding: utf-8 -*-

from master import setup


if __name__ == "__main__":
    config = {}

    config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@postgres/master"
    config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app = setup(**config)
    app.run(host="0.0.0.0", port=5000, debug=True)
