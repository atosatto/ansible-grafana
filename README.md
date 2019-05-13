Ansible Role: Grafana
==========================

[![Build Status](https://travis-ci.org/atosatto/ansible-grafana.svg?branch=master)](https://travis-ci.org/atosatto/ansible-grafana)
[![Galaxy](https://img.shields.io/badge/galaxy-atosatto.grafana-blue.svg?style=flat-square)](https://galaxy.ansible.com/atosatto/grafana)

Install and configure Grafana.

Requirements
------------

An Ansible 2.2 or higher installation.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    grafana_install_repo: "{{ grafana_repo_stable }}"

The APT/YUM repository from where to get Grafana packages.
By default, the official stable repository is used as defined in `vars/main.yml`.

    grafana_release_tag: ""

The Grafana release to be installed.
Set it to "latest" to install the latest stable release (see https://github.com/grafana/grafana/releases).

    grafana_user: "grafana"
    grafana_group: "grafana"

Grafana system user and group.

    grafana_admin_user: "admin"
    grafana_admin_password: "admin"

Grafana administration user name and  credentials.

    grafana_paths_data: "/var/lib/grafana"

Location of Grafana temp files, sessions, and the sqlite3 db.

    grafana_paths_logs: "/var/log/grafana"

Location of Grafana log files.

    grafana_paths_plugins: "/var/lib/grafana/plugins"

Directory where Grafana will automatically scan and look for plugins.

    grafana_paths_provisioning: "/etc/grafana/provisioning"

Location of the provisioning config files that Grafana will apply on startup. This feature is only available on Grafana >= 5.0.
See http://docs.grafana.org/administration/provisioning/ for additional information.

    grafana_server_http_addr: ""

The IP address Grafana will bind to. By default it will bind to all interfaces.

    grafana_server_http_port: "3000"

The port Grafana will bind to.

    grafana_server_root_url: "http://localhost:3000"

The full URL used to access Grafana from a web browser.
This is important when using OAUTH authentication.

    grafana_server_router_logging: "false"

Set to true for Grafana to log all HTTP requests (not just errors). These are logged as Info level events to grafana log.

    grafana_database_type: "sqlite3"
    grafana_database_host: "127.0.0.1:3306"
    grafana_database_name: "grafana"
    grafana_database_user: "root"
    grafana_database_password: ""
    grafana_database_ssl_mode: "disable"
    grafana_database_path: "grafana.db"

Configuration of the Grafana database to store users and dashboards.
By default, `sqlite3` will be configured and used.

    grafana_dashboards_versions_to_keep: "20"

Number of versions of the Grafana dashboards to keep.

    grafana_users_allow_sign_up: "false"

Set to `true` to allow users sign up / accounts creation.

    grafana_users_allow_org_create: "false"

Set to `true` to allow users to create new organizations.

    grafana_users_auto_assign_org: "false"

Set to `true` to automatically add new users to the provided organization.

    grafana_users_auto_assign_org_id: "1"

Set this value to automatically add new users to the provided organization.

    grafana_users_auto_assign_org_role: "Viewer"

The role new users will be assigned for in the provided organization (if `grafana_users_auto_assign_org` is set to `true`).

    grafana_auth_disable_login_form: "false"

Set to `true` to disable (hide) the login form, useful if you use OAuth.

    grafana_auth_anonymous_enabled: "false"
    grafana_auth_anonymous_org_name: "Main Org."
    grafana_auth_anonymous_org_role: "Viewer"

Anonymous access configuration.

    grafana_auth_github_enabled: "false"
    grafana_auth_github_allow_sign_up: "true"
    grafana_auth_github_client_id: "some_id"
    grafana_auth_github_client_secret: "some_secret"
    grafana_auth_github_scopes: "user:email,read:org"
    grafana_auth_github_auth_url: "https://github.com/login/oauth/authorize"
    grafana_auth_github_token_url: "https://github.com/login/oauth/access_token"
    grafana_auth_github_api_url: "https://api.github.com/user"
    grafana_auth_github_team_ids: ""
    grafana_auth_github_allowed_organizations: ""

Github OAuth configuration.

    grafana_auth_google_enabled: "false"
    grafana_auth_google_allow_sign_up: "true"
    grafana_auth_google_client_id: "some_id"
    grafana_auth_google_client_secret: "some_secret"
    grafana_auth_google_scopes: "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    grafana_auth_google_auth_url: "https://accounts.google.com/o/oauth2/auth"
    grafana_auth_google_token_url: "https://accounts.google.com/o/oauth2/token"
    grafana_auth_google_api_url: "https://www.googleapis.com/oauth2/v1/userinfo"
    grafana_auth_google_allowed_domains: ""

Google OAuth configuration.

    grafana_auth_generic_oauth_enabled: "false"
    grafana_auth_generic_oauth_name: "OAuth"
    grafana_auth_generic_oauth_allow_sign_up: "true"
    grafana_auth_generic_oauth_client_id: "some_id"
    grafana_auth_generic_oauth_client_secret: "some_secret"
    grafana_auth_generic_oauth_scopes: "user:email,read:org"
    grafana_auth_generic_oauth_auth_url: "https://foo.bar/login/oauth/authorize"
    grafana_auth_generic_oauth_token_url: "https://foo.bar/login/oauth/access_token"
    grafana_auth_generic_oauth_api_url: "https://foo.bar/user"
    grafana_auth_generic_oauth_team_ids: ""
    grafana_auth_generic_oauth_allowed_organizations: ""

Generic OAuth configuration.

    grafana_smtp_enabled: "false"
    grafana_smtp_host: "localhost:25"
    grafana_smtp_user: ""
    grafana_smtp_password: ""
    grafana_smtp_cert_file: ""
    grafana_smtp_key_file: ""
    grafana_smtp_skip_verify: "false"
    grafana_smtp_from_address: "admin@grafana.localhost"
    grafana_smtp_from_name: "Grafana"

Email server settings.

    grafana_log_mode: "console file"

Either `console`, `file`, `syslog`. Use space to separate multiple modes.

    grafana_log_level: "info"

Either `debug`, `info`, `warn`, `error`, `critical`.

    grafana_alerting_enabled: "true"

Set to `false` to disable alerting engine and hide Alerting from UI.

    grafana_alerting_execute_alerts: "true"

Makes it possible to turn off alert rule execution.

    grafana_datasources: []
    # grafana_datasources:
    # - name: "prometheus"
    #   type: "prometheus"
    #   access: "proxy"
    #   url: "http://127.0.0.1:9090"
    #   basicAuth: "false"

Automatically provision Grafana datasources using http://docs.grafana.org/administration/provisioning/#datasources.
**NB:** This feature required Grafana >= 5.0

    grafana_dashboards: []
    # grafana_dasboards:
    # - name: "prometheus"
    #   orgId: 1
    #   folder: ""
    #   type: file
    #   disableDeletion: false
    #   updateIntervalSeconds: 3
    #   editable: true
    #   options:
    #     path: /var/lib/grafana/dashboards

Automatically provision Grafana datashboards using http://docs.grafana.org/administration/provisioning/#dashboards.
The example above will configure Grafana to automatically load from the filesystem any dashboard available in `/var/lib/grafana/dashboards`.

Dependencies
------------

None.

Example Playbooks
-----------------

    $ cat playbook.yml
    - name: "Install and configure Grafana"
      hosts: all
      roles:
        - { role: atosatto.grafana }

Testing
-------

Tests are automated with [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ pip install tox

To test all the scenarios run

    $ tox

To run a custom molecule command

    $ tox -e py27-ansible25 -- molecule test -s grafana-lastest

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
