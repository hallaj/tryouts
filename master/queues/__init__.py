#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pika import BlockingConnection, ConnectionParameters, PlainCredentials

components = ["users", "settings"]


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
        self.channel.exchange_declare(exchange=name, type="direct")

        for component in components:
            queue = name + "_" + component
            self.channel.queue_declare(queue=queue)
            self.channel.queue_bind(exchange=name, queue=queue,
                                    routing_key=component)

    def delete(self, name):
        self.channel.exchange_delete(exchange=name)

        for component in components:
            queue = name + "_" + component
            self.channel.queue_delete(queue=queue)
