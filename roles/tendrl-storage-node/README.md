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

 *  Variable `etcd_ip_address` needs to be set to ipv4 adress of etcd instance.
    Specifying this variable is mandatory as there is no default value.

 *  Variable `graphite_ip_address` needs to be set to ipv4 adress of graphite
    instance. Specifying this variable is mandatory as there is no default
    value.

 *  When `etcd_authentication` variable is undefined or set to `True` (which is
    the default value), this role will specify etcd username and password in
    tendrl config files.

    When the value of `etcd_authentication` is `False`, ansible tasks which
    configures etcd credentials will be just skipped.
    In other words, **this role can't disable or reconfigure etcd
    authentication, it can only skip auth config tasks**.

    For production, keep the authentication always enabled.

Note that values specified in variables of this role need to match variables
of *Tendrl Server* role.

License
-------

GNU Lesser General Public License, version 2.1
