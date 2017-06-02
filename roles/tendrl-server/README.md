Tendrl Server
=============

This role automates installation of *Tendrl Server*, as described in *Server
Installation* section of [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

Requirements
------------

This role expects that the repositories with Tendrl packages (and it's
dependencies) is already available on the machine.

Role Variables
--------------

* When `etcd_ip_address` variable is undefined (which is the default state),
  this role will use ip address of default ipv4 network interface to configure
  etcd, otherwise a value of this variable will be used.

License
-------

Apache 2.0
