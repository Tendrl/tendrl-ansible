Ceph Installer
==============

This role automates installation of [Ceph
Installer](http://docs.ceph.com/ceph-installer/docs/), which consists of two
steps:

* Enabling all required rpm repositories (one for `ceph-installer`, another for
  `ceph-ansible` and [copr](https://docs.pagure.org/copr.copr/user_documentation.html#faq)
  repository
  [ktdreyer/ceph-installer](https://copr.fedorainfracloud.org/coprs/ktdreyer/ceph-installer/)
  with additional dependencies).
* Installation of the `ceph-installer` package itself

No further configuration of ceph-installer is performed in this role, the
package is just installed.

Use this role along with role *Tendrl Server* if you plan to provision Ceph
clusters via Tendrl.

Requirements
------------

Expected to be used on CentOS 7 machine.

Role Variables
--------------

* Predefined variable `ceph_installer_baseurl` contains url of repository
  with `ceph-installer` package.
* Predefined variable `ceph_ansible_baseurl` contains url of repository with
  `ceph-ansible` package.

License
-------

GNU Lesser General Public License, version 2.1
