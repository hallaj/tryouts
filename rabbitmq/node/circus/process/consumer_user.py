#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from msgpack import unpackb
from os.path import dirname, join
from pika import BlockingConnection, ConnectionParameters, PlainCredentials


def insert(**record):
    from sys import path
    path.append("/srv")

    from node import setup
    from node.models import db
    from node.models.user import User

    config = {}

    config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@postgres/node"
    config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app = setup(**config)

    db.init_app(app)
    db.app = app

    user = User.query.filter_by(username=record["username"])

    if not user or user.count() != 1:
        user = User(**record)
        db.session.add(user)
    else:
        user = user.one()
        user.name = record["name"]

    db.session.commit()


config_file = join(dirname(__file__), "config.json")
config = loads(open(config_file).read())

credentials = PlainCredentials(config["mq_user"], config["mq_pass"])
parameters = ConnectionParameters(host=config["mq_host"],
                                  credentials=credentials)
connection = BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue="%s_users" % config["node_name"])


def callback(ch, method, properties, body):
    data = unpackb(body, encoding="utf-8")
    insert(**data)

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue="%s_users" % config["node_name"])
channel.start_consuming()
