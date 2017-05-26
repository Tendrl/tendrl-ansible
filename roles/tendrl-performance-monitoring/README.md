Tendrl Performance Monitoring
=============================

This role automates installation of *Tendrl Performance Monitoring* component,
as described in *Performance Monitoring installation* section in [Tendrl
Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference)

Requirements
------------

This role expects that the repositories with Tendrl packages (and it's
dependencies) are already available on the machine.

Moreover we expect that *Tendrl Server* role will be installed somewhere
(on that machine, etcd and tendrl-api will be running).

Role Variables
--------------

You need to define all variables listed there, with references to other
services:

* `etcd_ip_address`: ipv4 address of etcd instance
* `tendrl_api_ip_address`: ipv4 address of `tendrl-api` service

Note that by default, both services will be running on a single *Tendrl
Server* machine (this distinction is here so that you can use this role even
when you decide to have mentioned services listening on different interfaces).

License
-------

Apache 2.0
