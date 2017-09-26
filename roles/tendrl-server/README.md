Tendrl Server
=============

This role automates installation of *Tendrl Server*, as described in *Server
Installation* section of [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

Please note this role automates setup of admin user account for Tendrl (usable
with both api and web interface), and that new random default password is
stored on *Tendrl Server* machine in `/root/password` file (based on
[TEN-257](https://tendrl.atlassian.net/browse/TEN-257)).

Also note that this role enables [etcd
authentication](https://coreos.com/etcd/docs/latest/op-guide/authentication.html)
by default (see description of `etcd_authentication` variable below), creating
etcd root user account with new default random password via [ansible password
lookup
plugin](https://docs.ansible.com/ansible/latest/playbooks_lookups.html#the-password-lookup).
This means that the password of etcd root user will be stored in current working
directory (from where you run ansible), in `etcd_root_passwd` file. Don't
delete this password file, as this role can't regenerate etcd root password.

Moreover it also generates new random password for grafana admin user account
via [ansible password lookup
plugin](https://docs.ansible.com/ansible/latest/playbooks_lookups.html#the-password-lookup),
which is then stored in `grafana_admin_passwd` file in current working
directory. To regenerate this password, you can safely delete this password
lookup file and rerun the playbook, new password will be generated and all
affected components reconfigured.

Requirements
------------

This role expects that the repositories with Tendrl packages (and it's
dependencies) are already available on the machine.

If you want to be able to provision Ceph clusters with Tendrl, use role
*Ceph Installer* on the same machine as this role.

Role Variables
--------------

 *  When `etcd_ip_address` variable is undefined (which is the default state),
    this role will use ip address of default ipv4 network interface to
    configure etcd, otherwise a value of this variable will be used.

 *  When `graphite_ip_address` variable is undefined (which is the default
    state), this role will use ip address of default ipv4 network interface,
    otherwise a value of this variable will be used.

 *  When `graphite_port` variable is undefined, task which configures graphite
    port for `tendrl-node-agent` will be skipped so that the default value from
    config file (as shipped in rpm package) will be used. *If you are not sure*
    if you need to reconfigure this, *leave this variable undefined*.

 *  When `httpd_ip_address` variable is undefined,

    TODO:

 *  When `httpd_server_name` variable is undefined,

    TODO:

 *  When `etcd_authentication` variable is undefined or set to `False` (which
    is the default value), ansible would just skip all etcd authentication
    tasks (icluding both etcd auth setup and tendrl configuration),
    which means that if the etcd auth has been already enabled, it will still
    be enabled and when etcd auth is disabled, it will continue to be disabled.
    In other words, **this role can't disable nor reconfigura etcd
    authentication, it can only skip etcd auth setup and config tasks**.

    Since authentication is disabled in etcd by default, the only way to
    configure Tendrl to run without etcd authentication is to set
    `etcd_authentication` to `False` for the 1st time you run ansible to deploy
    Tendrl, and keep it this way every other run of tendrl-ansible.

    When the value is `True`, this role will enable [etcd
    authentication](https://coreos.com/etcd/docs/latest/op-guide/authentication.html)
    and configure tendrl components accordingly.

 *  When one or both of variables `tendrl_notifier_email_id` and
    `tendrl_notifier_email_smtp_server` is undefined (which is
    the default state for both variables), email configuration of
    tendrl-notifier is skipped.

    Only when both these variables are defined, email configuration of
    tendrl-notifier is performed.

    Values provided here are used for configuration of `email_id` and
    `email_smtp_server` options in `/etc/tendrl/notifier/email.conf.yaml`
    config file.

    Tendrl notifier uses value of `email_id` as a source email address when
    sending notification messages via email.

    For more details about email configuration of tendrl-notifier, see the
    Tendrl documentation.

 *  When `tendrl_notifier_email_smtp_port` variable is undefined, default value
    `25` will be used.

    Value provided here is used for configuration of `email_smpt_port` option
    in `/etc/tendrl/notifier/email.conf.yaml` config file.

    Note that this value is used only when both
    `tendrl_notifier_email_smtp_server` and `tendrl_notifier_email_id` are
    defined.

 *  When `tendrl_notifier_email_auth` variable is defined, it's value will
    be used to configure `auth` option in
    `/etc/tendrl/notifier/email.conf.yaml` file.

    When the variable is undefined, no configuration change of `auth` option
    will be performed.

    For more details about email configuration of tendrl-notifier, see the
    Tendrl documentation.

 *  When `tendrl_notifier_email_pass` variable is defined, it's value will
    be used to configure `email_pass` option in
    `/etc/tendrl/notifier/email.conf.yaml` file.

    When the variable is undefined, no configuration change of `email_pass`
    option will be performed.

    Tendrl notifier uses value of `email_pass` as smtp password which is
    used along with `email_id` value as an smpt username to login into
    `email_smtp_server`, so that the notifier can send email messages with
    notifications with `email_id` source address using authenticated smpt
    server.

    For more details about email configuration of tendrl-notifier, see the
    Tendrl documentation.

 *  When `tendrl_ssl_enabled` variable is undefined or set to `False` (which
    is the default value), ansible would not configure tendrl to provide
    web interface including REST API over SSL encripted connection.

    When `tendrl_ssl_enabled` variable is set to `True`, SSL will be enabled
    for Tendrl web interface including API.

 *  When one or both of variables `httpd_ssl_certificate_file` and
    `httpd_ssl_certificate_key_file` is undefined (which is
    the default state for both variables), the self signed local SSL key
    created during installation of `mod_ssl` package will be used.

    Value of `http_ssl_certificate_file` variable is used as
    `SSLCertificateFile`, and `httpd_ssl_certificate_key_file` as
    `SSLCertificateKeyFile`.

    To use different SSL certificate, you need to create it and place it on the
    tendrl server yourself, and then use it's absolute file path on tendrl
    server as value for both variables.

License
-------

GNU Lesser General Public License, version 2.1
