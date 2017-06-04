#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, abort, redirect, render_template, request, url_for

from ...models import db
from ...models.nodes import Nodes

admin_nodes = Blueprint("admin_nodes", __name__)


@admin_nodes.route("/admin/nodes", methods=["GET", "POST"])
def admin_nodes_index():
    if request.method == "POST":
        name = request.form.get("node_name")

        if not name:
            abort(500)

        node = Nodes(name=name)
        db.session.add(node)
        db.session.commit()

    records = Nodes.query.all()
    return render_template("admin/nodes/index.tpl", nodes=records)


@admin_nodes.route("/admin/nodes/delete", methods=["POST"])
def admin_nodes_delete():
    id_ = request.form.get("node_id")

    if not id_:
        abort(500)

    node = Nodes.query.filter_by(id_=id_)

    if not node or node.count() != 1:
        abort(500)

    db.session.delete(node.one())
    db.session.commit()

    return redirect(url_for("admin_nodes.admin_nodes_index"))
