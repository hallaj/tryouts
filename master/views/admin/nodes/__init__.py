#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, redirect, render_template, request, url_for

from master.models import db
from master.models.node import Node
from master.models.user import User
from master.queues import Queues

admin_nodes = Blueprint("admin_nodes", __name__)


@admin_nodes.route("/admin/nodes", methods=["GET", "POST"])
def admin_nodes_index():
    if request.method == "POST":
        name = request.form.get("node_name")

        if not name:
            abort(500)

        node = Node(name=name)
        db.session.add(node)
        db.session.commit()

        queue = Queues()
        queue.declare(name)
        queue.close()

    records = Node.query.all()
    return render_template("admin/nodes/index.tpl", nodes=records)


@admin_nodes.route("/admin/nodes/<node_id>/info")
def admin_nodes_info(node_id=None):
    if not node_id:
        abort(404)

    node = Node.query.filter_by(id_=node_id)

    if not node or node.count() != 1:
        abort(500)

    node = node.one()
    users = User.query.filter_by(node_id=node_id)

    return render_template("admin/nodes/info.tpl", node=node, users=users)


@admin_nodes.route("/admin/nodes/delete", methods=["POST"])
def admin_nodes_delete():
    id_ = request.form.get("node_id")

    if not id_:
        abort(500)

    node = Node.query.filter_by(id_=id_)

    if not node or node.count() != 1:
        abort(500)

    node = node.one()
    name = node.name

    db.session.delete(node)
    db.session.commit()

    queue = Queues()
    queue.delete(name)

    return redirect(url_for("admin_nodes.admin_nodes_index"))
