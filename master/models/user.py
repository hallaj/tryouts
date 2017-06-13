#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = (db.UniqueConstraint("username", "node_id"), {})

    id_ = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    username = db.Column("username", db.String(100), nullable=False)
    password = db.Column("password", db.String(100), nullable=False, unique=True)
    node_id = db.Column("node_id", db.Integer, db.ForeignKey("node.id"))
