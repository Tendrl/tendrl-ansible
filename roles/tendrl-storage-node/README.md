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

* Variable `etcd_ip_address` needs to be set to ipv4 adress of etcd instance.
  Specifying this variable is mandatory as there is no default value.
* Variable `graphite_ip_address` needs to be set to ipv4 adress of graphite
  instance. Specifying this variable is mandatory as there is no default value.

License
-------

Apache 2.0
