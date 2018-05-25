Tendrl Server
=============

This role automates installation of *Tendrl Server*, as described in *Server
Installation* section of [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

Please note this role automates setup of admin user account for Tendrl (usable
with both api and web interface), and that new random default password is
stored on *Tendrl Server* machine in `/root/password` file (based on
[TEN-257](https://tendrl.atlassian.net/browse/TEN-257)).

Also note that this role
also generates new random password for grafana admin user account
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

 *  Variable `etcd_ip_address` is mandatory, when you let this variable
    undefined, installation will fail.

    Value of `etcd_ip_address` is used to configure where etcd instance is
    listening.

    If you provide a hostname instead of an ip address there, etcd instance may
    fail to even start. Note that etcd upstream requires to use ip address for
    this configuration.

 *  Variable `etcd_fqdn` is mandatory, when you let this variable undefined,
    installation will fail.

    Value of this variable is used to configure tendrl components to be able
    to connect to etcd instance (aka tednrl central store).

    If you provide an ip address instead of fqdn there, tendrl components
    may fail to start or even crash. Note that etcd upstream requires to use
    fqdn for this configuration. See:

    https://github.com/Tendrl/commons/issues/759

 *  Variable `graphite_fqdn` is mandatory, when you let this variable undefined,
    installation will fail.

    Value of this variable is used to configure tendrl components
    (this value doesn't reconfigure graphite itself!) to be able to connect to
    graphite instance (carbon-cache service in particular).

 *  When `graphite_port` variable is undefined, task which configures graphite
    port for `tendrl-node-agent` will be skipped so that the default value from
    config file (as shipped in rpm package) will be used. *If you are not sure*
    if you need to reconfigure this, *leave this variable undefined*.

 *  When `etcd_tls_client_auth` is set to False (which is the default state),
    etcd will work without any authentication (default etcd behavior).

    When `etcd_tls_client_auth` is True, etcd will be reconfigured to use
    client to server authentication with HTTPS client certificates, and all
    Tendrl components will be reconfigured accordingly.

    Note that tendrl-ansible is not concerned with issuing and deployment of
    certificates. So for etcd tcl client authentication to work, *you need to
    issue and deploy tls certificates for all machines of the Tendrl cluster*
    (including storage nodes and Tendrl server) *before running
    tendrl-ansible*.

    The placement of tls cert files can be tweaked via ansible variables
    explained below.

    For more details, see:

    * [Red Hat Enterprise Linux 7 - Security Guide - Using OpenSSL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-using_openssl)
    * [Etcd Security model](https://coreos.com/etcd/docs/latest/op-guide/security.html)

 *  Variable `etcd_cert_file` specifies full filepath of `ETCD_CERT_FILE` etcd
    option. The default value is `/etc/pki/tls/certs/etcd.crt`.

    For more details, see [Etcd Security
    model](https://coreos.com/etcd/docs/latest/op-guide/security.html)

 *  Variable `etcd_key_file` specifies full filepath of `ETCD_KEY_FILE` etcd
    option. The default value is `/etc/pki/tls/private/etcd.key`.

    For more details, see [Etcd Security
    model](https://coreos.com/etcd/docs/latest/op-guide/security.html)

 *  Variable `etcd_trusted_ca_file` specifies full filepath of
    `ETCD_TRUSTED_CA_FILE` etcd option. The default value is
    `/etc/pki/tls/certs/ca-etcd.crt`.

    For more details, see [Etcd Security
    model](https://coreos.com/etcd/docs/latest/op-guide/security.html)

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

 *  When `tendrl_notifier_snmp_conf_file` variable is undefined, tendrl
    notifier will not send any snmp notifications, which is the default state.

    To configure snmp notifications, create new `snmp.conf.yaml` file
    based on default `/etc/tendrl/notifier/snmp.conf.yaml` file from
    tendrl-notifier package, and set it's local path (on ansible control
    machine) as a value of `tendrl_notifier_snmp_conf_file` variable.

    Based on that, tendrl-ansible will then copy the local file into
    `/etc/tendrl/notifier/snmp.conf.yaml` on tendrl server and restart
    tendrl-notifier service.

    For more details (including supported versions of snmp protocol and example
    configuration of snmp endpoint), see Tendrl Installation Guide.

 *  When `configure_firewalld_for_tendrl` is set to True (which is the default
    state), ports necessary for Tendrl to work will be opened via
    [firewalld](http://www.firewalld.org/).
    Note that *tendrl-ansible aborts playbook run when firewalld is not
    running* on the machines, preventing accidental blocking of services which
    are already running on the cluster.

    When `configure_firewalld_for_tendrl` is False, tendrl-ansible will skip
    all firewall
    tasks completelly. This is usefull if you want to maintain firewall
    configuration yourself (eg. via iptables scripts, having firewall disabled
    ...). Note that in this case, you are responsible for opening ports of
    all services running on the cluster, including Gluster and Tendrl.

    For list of Tendrl ports, see [Tendrl firewall
    settings](https://github.com/Tendrl/documentation/wiki/Tendrl-firewall-settings)
    wikipage.

License
-------

GNU Lesser General Public License, version 2.1
