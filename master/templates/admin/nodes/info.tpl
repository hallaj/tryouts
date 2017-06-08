{% extends "base.tpl" %}

{% block content %}
<section class="section">
  <div class="container">
    <div class="heading">
      <h2 class="title">Administration :: Nodes :: Info</h2>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="heading">
        <h2 class="subtitle">Node Information: {{ node.name }}</h2>
      </div>

      <div class="section">
        <p>Node Name: {{ node.name }}</p>
      </div>

      <div class="section">
        <div class="container">
          <div class="heading">
            <h2 class="subtitle">Users</h2>
          </div>

          <div class="section">
            {% if users %}
            <table class="table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Username</th>
                </tr>
              </thead>

              <tbody>
                {% for user in users %}
                <tr>
                  <td>{{ user.name }}</td>
                  <td>{{ user.username }}</td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
            {% else %}
            <p>No users found under this node</p>
            {% endif %}
          </div>

          <section class="section">
            <div class="container">
              <div class="heading">
                <h2 class="subtitle">Add user</h2>
              </div>
            </div>

            <div class="section">
              <form action="{{ url_for('admin_users.admin_users_add') }}" method="post">
                <div class="field">
                  <label class="label">Name</label>

                  <p class="control">
                    <input class="input" name="name" placeholder="Name" type="text" />
                  </p>
                </div>

                <div class="field">
                  <label class="label">Username</label>

                  <p class="control">
                    <input class="input" name="username" placeholder="Username" type="text" />
                  </p>
                </div>

                <div class="field">
                  <label class="label">Password</label>

                  <p class="control">
                    <input class="input" name="password" placeholder="Password" type="password" />
                  </p>
                </div>

                <div class="field">
                  <p class="control">
                    <input type="hidden" name="node_id" value="{{ node.id_ }}" />
                    <input class="button" type="submit" value="Add" />
                  </p>
                </div>
              </form>
            </div>
          </section>
        </div>
      </div>
    </div>
  </section>

</section>
{% endblock %}
