#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pika import BlockingConnection, ConnectionParameters, PlainCredentials


class Queues(object):
    def __init__(self):
        credentials = PlainCredentials("admin", "admin")
        parameters = ConnectionParameters(host="rabbitmq",
                                          credentials=credentials)
        self.connection = BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def close(self):
        self.connection.close()

    def declare(self, name):
        self.channel.queue_declare(queue=name)

    def delete(self, name):
        self.channel.queue_delete(queue=name)
