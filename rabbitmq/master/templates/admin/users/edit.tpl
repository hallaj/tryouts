{% extends "base.tpl" %}

{% block content %}
<section class="section">
  <div class="container">
    <div class="heading">
      <h2 class="title">Administration :: Users :: Edit</h2>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="heading">
        <h2 class="subtitle">User Information: {{ user.name }}</h2>
      </div>

      <div class="section">
        <form action="{{ url_for('admin_users.admin_users_edit', user_id=user.id_) }}" method="post">
          <div class="field">
            <label class="label">Name</label>

            <p class="control">
              <input class="input" name="name" type="text" value="{{ user.name }}" />
            </p>
          </div>

          <div class="field">
            <label class="label">Username</label>

            <p class="control">
              <input class="input" disabled name="username" type="text" value="{{ user.username }}" />
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
              <input class="button" type="submit" value="Save" />
            </p>
          </div>
        </form>
      </div>
    </div>
  </section>
</section>
{% endblock %}
