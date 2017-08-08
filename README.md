tendrl-ansible
==============

Ansible playbook for [Tendrl](http://tendrl.org/)!

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
   (required on Ceph or Gluster servers, which you would like to manage by
   Tendrl)

Please note that `tendrl-server` role includes setup of admin user account for
Tendrl (usable with both api and web interface), and that new random default
password is stored on *Tendrl Server* machine in `/root/password` file (based
on [TEN-257](https://tendrl.atlassian.net/browse/TEN-257)).

For convenience, there are also ansible roles for installation of yum
repositories with upstream releases of Ceph, Gluster and theirs installation
tools (such as `ceph-installer` and `gdeploy`):

* `ceph-installer`
* `gluster-gdeploy-copr`

See sample ansible playbook `site.yml.sample` to check how it fits together.

## Basic setup

Ansible Driven installation:

* Step 1: Install Ansible >= 2.2
* Step 2: Git the code:        `git clone https://github.com/Tendrl/tendrl-ansible.git`
* Step 3: Set up the Ansible groups in inventory file:
          `[ tendrl-server]       [ceph-servers]        [gluster-servers]`
* Step 3: Create `site.yml` file based on `site.yml.sample` and make sure to
  define `etcd_ip_address` and `tendrl_api_ip_address` to suit
* Step 4: Run `# ansible-playbook site.yml`
* Step 5: ssh into your Tendrl server as root and `cat /root/password` 
* Step 6: log in to your tendrl server at http://ip.of.tendrl.server  with admin user and the password from step 5

## Setup with Vagrant using libvirt provider

TODO

## Setup with Vagrant using virtualbox provider

TODO
