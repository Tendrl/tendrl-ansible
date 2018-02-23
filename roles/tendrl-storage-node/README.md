Tendrl Storage Node
===================

This role automates installation of *Tendrl Storage Node*, as described in
*Storage Node Installation* section of [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

Requirements
------------

This role expects that the repositories with Tendrl packages (and it's
dependencies) are already available on the machine.

Role Variables
--------------

 *  Variable `etcd_fqdn` needs to be set to fqdn of etcd instance.
    Specifying this variable is mandatory as there is no default value.

 *  Variable `graphite_fqdn` needs to be set to fqdn of graphite
    instance. Specifying this variable is mandatory as there is no default
    value.

 *  When `etcd_tls_client_auth` is set to False (which is the default state),
    tendrl components will be configured to work with etcd without any
    authentication (default etcd behavior).

    When `etcd_tls_client_auth` is True, all Tendrl components will be
    reconfigured to use client to server authentication with HTTPS client
    certificates.

    The placement of tls cert files can be tweaked via ansible variables
    explained below.

    For more details, see README file of tendrl server ansible role.

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

 *  When `configure_firewalld_for_tendrl` is set to True (which is the default
    state), ports necessary for Tendrl to work will be opened via
    [firewalld](http://www.firewalld.org/).
    Note that *tendrl-ansible aborts playbook run when firewalld is not
    running* on the machines, preventing accidental blocking of services which
    are already running on the cluster.

    When `etcd_tls_client_auth` is False, tendrl-ansible will skip all firewall
    tasks completelly. This is usefull if you want to maintain firewall
    configuration yourself (eg. via iptables scripts, having firewall disabled
    ...). Note that in this case, you are responsible for opening ports of
    all services running on the cluster, including Gluster and Tendrl.

    For list of Tendrl ports, see [Tendrl firewall
    settings](https://github.com/Tendrl/documentation/wiki/Tendrl-firewall-settings)
    wikipage.

Note that values specified in variables of this role need to match variables
of *Tendrl Server* role.

License
-------

GNU Lesser General Public License, version 2.1
