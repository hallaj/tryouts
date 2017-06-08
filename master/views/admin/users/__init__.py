#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, jsonify, redirect, request, url_for
from msgpack import packb
from werkzeug.security import generate_password_hash

from master.models import db
from master.models.node import Node
from master.models.user import User
from master.queues import Queues


admin_users = Blueprint("admin_users", __name__)


@admin_users.route("/admin/users/add", methods=["POST"])
def admin_users_add():
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    node_id = request.form.get("node_id")

    if not username or not password:
        abort(500)

    password = generate_password_hash(password)

    node = Node.query.filter_by(id_=node_id)

    if not node or node.count() != 1:
        abort(500)

    node = node.one()
    user = User(name=name, username=username, password=password,
                node_id=node_id)

    db.session.add(user)
    db.session.commit()

    user = packb({"name": name, "username": username, "password": password,
                  "node_id": node_id})

    queue = Queues()
    queue.publish(node.name, "users", user)

    return redirect(url_for("admin_nodes.admin_nodes_info", node_id=node_id))
