#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db


class Node(db.Model):
    __tablename__ = "node"

    id_ = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), unique=True)
    users = db.relationship("User", backref="node", lazy="dynamic")
