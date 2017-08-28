Tendrl Storage Node
===================

This role automates installation of *Tendrl Storage Node*, as described in
*Storage Node Installation* section of [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

Requirements
------------

This role expects that the repositories with Tendrl packages (and it's
dependencies) are already available on the machine.

If you want to be able to provision Ceph clusters with Tendrl, make Ceph
rpm repositories (for ceph-mon and ceph-osd) available on *Tendrl Storage Node*
machines.

If you want to be able to provision Gluster clusters with Tendrl, make *Gluster
Gdeploy* rpm repository available on *Tendrl Storage Node* machines and
update related role variables (see details below).

Role Variables
--------------

* Variable `etcd_ip_address` needs to be set to ipv4 adress of etcd instance.
  Specifying this variable is mandatory as there is no default value.
* Variable `graphite_ip_address` needs to be set to ipv4 adress of graphite
  instance. Specifying this variable is mandatory as there is no default value.

License
-------

Apache 2.0
