#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from master import setup


config = {}

config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@postgres/master"
config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def bootstrap():
    from master.models import db
    from master.models.node import Node
    from master.models.user import User

    app = setup(**config)
    db.init_app(app=app)
    db.create_all(app=app)


if __name__ == "__main__":
    parser = ArgumentParser(description="Master application")
    parser.add_argument("command")

    args = parser.parse_args()

    if args.command == "bootstrap":
        bootstrap()
    else:
        app = setup(**config)
        app.run(host="0.0.0.0", port=5000, debug=True)
