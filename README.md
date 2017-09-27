tendrl-ansible
==============

Ansible roles and playbooks for [Tendrl](http://tendrl.org/)!

Clone me:

```bash
git clone https://github.com/Tendrl/tendrl-ansible.git
```


**NOTE:** The `master` branch was completely overwritten on 13th June 2017. The original master branch is now available as the branch `archive`.


## What does it do?

There are ansible roles for installation of [Tendrl](http://tendrl.org/), based
on [upstream documentation](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference):

* `tendrl-copr`: installs yum repository of latest Tendrl upstream release
* `tendrl-server`: installation of *Tendrl Server* machine (where api, web and
   etcd are running)
* `tendrl-storage-node`: installation of *Tendrl Storage Node* machine
   (required on Gluster servers, which you would like to monitor by
   Tendrl)

Please note that `tendrl-server` role includes setup of admin user account for
Tendrl (usable with both api and web interface), and that default
password is ``adminuser``. Moreover the admin password is also
stored on *Tendrl Server* machine in `/root/password` file (this feature of
tendrl-ansible is based
on [TEN-257](https://tendrl.atlassian.net/browse/TEN-257)).

For convenience, there are also ansible roles for installation of yum
repositories with upstream releases of Ceph, Gluster and theirs installation
tools (such as `ceph-installer` and `gdeploy`):

* `ceph-installer`
* `gluster-gdeploy-copr`

See sample ansible playbook `site.yml.sample` to check how it fits together.

## Basic setup

Ansible Driven installation:

1) Install Ansible >= 2.2
2) Get the code: `git clone https://github.com/Tendrl/tendrl-ansible.git`
3) Create Ansible inventory file with groups for `tendrl-server`
   and `gluster-servers`. Here is an example of inventory
   file for 4 node cluster with Gluster:

```
[gluster-servers]
gl1.example.com
gl2.example.com
gl3.example.com
gl4.example.com

[tendrl-server]
tendrl.example.com
```

4) Create `site.yml` file based on `site.yml.sample` and make sure to
   define `etcd_ip_address` to suit
5) Run `$ ansible-playbook -i inventory_file site.yml`
6) Log in to your tendrl server at ``http://ip.of.tendrl.server`` with
   ``admin`` user and the default password ``adminuser``.

## Setup with Vagrant using libvirt provider

TODO

## Setup with Vagrant using virtualbox provider

TODO

## License

Distributed under the terms of the [GNU LGPL, version
2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) license,
tendrl-ansible is free and open source software.
