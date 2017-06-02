Tendrl Server
=============

This role automates installation of *Tendrl Server*, as described in *Server
Installation* section of [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

This role also includes installation and setup of *Tendrl Alerting*, which is
described in another section of the documentation linked above, because
deploying it on the *Tenrl Server* machine is a safe default choice (moreover
we try to limit sheer number of possible deployment scenarios until more
complicated architectures and scaling will be documented and tested).

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

License
-------

Apache 2.0
