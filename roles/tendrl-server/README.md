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
directory (from where you run ansible), in `etcd_root_passwd` file.

Requirements
------------

This role expects that the repositories with Tendrl packages (and it's
dependencies) are already available on the machine.

If you want to be able to provision Ceph clusters with Tendrl, use role
*Ceph Installer* on the same machine as this role.

Role Variables
--------------

* When `etcd_ip_address` variable is undefined (which is the default state),
  this role will use ip address of default ipv4 network interface to configure
  etcd, otherwise a value of this variable will be used.
* When `graphite_ip_address` variable is undefined (which is the default
  state), this role will use ip address of default ipv4 network interface,
  otherwise a value of this variable will be used.
* When `graphite_port` variable is undefined, task which configures graphite
  port for `tendrl-node-agent` will be skipped so that the default value from
  config file (as shipped in rpm package) will be used. *If you are not sure*
  if you need to reconfigure this, *leave this variable undefined*.
* When `etcd_authentication` variable is undefined or set to `True` (which is
  the default value), this role will configure [etcd
  authentication](https://coreos.com/etcd/docs/latest/op-guide/authentication.html).
  When the value is `False`, the authentication will be disabled, which is
  useful for development/testing purposes only. For production, keep the
  authentication always enabled.

License
-------

Apache 2.0
