#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import db


class Nodes(db.Model):
    __tablename__ = "nodes"

    id_ = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(20), unique=True)
