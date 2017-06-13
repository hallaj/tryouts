#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db


class User(db.Model):
    __tablename__ = "user"

    id_ = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    username = db.Column("username", db.String(100), nullable=False, unique=True)
    password = db.Column("password", db.String(100), nullable=False)
