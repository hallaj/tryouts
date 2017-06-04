{% extends "base.tpl" %}

{% block content %}
<section class="section">
  <div class="container">
    <div class="heading">
      <h2 class="title">Administration :: Nodes</h2>
    </div>

    <section class="section">
      <div class="container">
        <div class="heading">
          <h2 class="subtitle">Available nodes</h2>
        </div>

        <div class="section">
          <table class="table">
            <thead>
              <tr>
                <th>Name</th>
              </tr>
            </thead>

            <tbody>
              {% for node in nodes %}
              <tr>
                <td>{{ node.name }}</td>
                <td>
                  <form action="{{ url_for("admin_nodes.admin_nodes_delete") }}" method="post">
                    <input name="node_id" type="hidden" value="{{ node.id_ }}" />

                    <span class="icon">
                      <button><i class="fa fa-trash"></i></button>
                    </span>
                  </form>
                </td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="heading">
          <h2 class="subtitle">Add node</h2>
        </div>

        <div class="section">
          <form action="{{ url_for('admin_nodes.admin_nodes_index') }}" method="post">
            <div class="field has-addons">
              <p class="control has-icons-left">
                <input class="input" name="node_name" type="text" />
                <span class="icon is-small is-left">
                  <i class="fa fa-cube"></i>
                </span>
              </p>
              <p class="control">
                <input class="button" type="submit" value="Add" />
              </p>
            </div>
          </form>
        </div>
      </div>
    </section>
  </div>
</section>
{% endblock %}
