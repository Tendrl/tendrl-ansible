tendrl-ansible
==============

Ansible playbook for [Tendrl](http://tendrl.org/)!

Clone me:

```bash
git clone https://github.com/Tendrl/tendrl-ansible.git
```

## What does it do?

There are ansible roles for installation of [Tendrl](http://tendrl.org/), based
on [upstream documentation](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference):

* `tendrl-copr`: installs yum repository of latest Tendrl upstream release
* `tendrl-server`: installation of *Tendrl Server* machine (where api, web and
   etcd are running)
* `tendrl-storage-node`: installation of *Tendrl Storage Node* machine
   (required on Ceph or Gluster servers, which you would like to manage by
   Tendrl)
* `tendrl-performance-monitoring`: installs *Tendrl Performance Monitoring*
   component

Please note that `tendrl-server` role includes setup of admin user account for
Tendrl (usable with both api and web interface), and that new random default
password is stored on *Tendrl Server* machine in `/root/password` file (based
on [TEN-257](https://tendrl.atlassian.net/browse/TEN-257)).

For convenience, there are also ansible roles for installation of yum
repositories with upstream releases of Ceph, Gluster and theirs installation
tools (such as `ceph-installer` and `gdeploy`):

* `ceph-installer`
* `gluster-gdeploy-copr`

See sample ansible playbook `site.yml.sample` to chekc how it fits together.

## Setup with Vagrant using libvirt provider

TODO

## Setup with Vagrant using virtualbox provider

TODO
