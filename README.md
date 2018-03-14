tendrl-ansible
==============

[Ansible](https://docs.ansible.com/ansible/latest/index.html) roles and
playbooks for [Tendrl](http://tendrl.org/)!


## What does it do?

tendrl-ansible automates **installation of Tendrl** and helps with **cluster
expansion** based description from
[Tendrl wiki](https://github.com/Tendrl/documentation/wiki). You
should check [installation documentation
there](https://github.com/Tendrl/documentation/wiki/Tendrl-release-latest) to
have basic understanding of various machine roles in Tendrl cluster before
using tendrl-ansible.


## How to get tendrl-ansible?

Just clone this repo:

```
$ git clone https://github.com/Tendrl/tendrl-ansible.git
```

or you can install rpm package from [copr repo `tendrl/release` with stable
Tendlr upstream
builds](https://copr.fedorainfracloud.org/coprs/tendrl/release/):

```
# yum copr enable tendrl/release
# yum install tendrl-ansible
```

See [how to enable copr
repository](https://docs.pagure.org/copr.copr/how_to_enable_repo.html#how-to-enable-repo)
if you need more help with this step.

Note that installing **tendrl-ansible from rpm package is highly recommended
when you use stable builds** from `tendrl/release` copr. Otherwise just cloning
the repo is good enough.


## Which version of ansible do I need?

Ansible >= 2.4 is required to use tendrl-ansible.


## What roles and playbooks are there?

This is a brief overview only, **there is a README file for each role**, where
you can see more details about each role, along with list of ansible variables
one can use to tweak it.

Ansible roles for Tendrl:

* `tendrl-ansible.tendrl-copr`: installs yum repositories with builds provided
  by Tendrl project, it uses stable `tendrl/release` copr by default
* `tendrl-ansible.tendrl-server`: installation of **Tendrl Server** machine
  (where Tendrl api, web and etcd are running)
* `tendrl-ansible.tendrl-storage-node`: installation of **Tendrl Storage Node**
  machines (Gluster servers, which you would like to monitor by Tendrl)

Roles installing yum repositories of Tendrl dependencies:

* `tendrl-ansible.grafana-repo`: installs official upstream yum repository with
  latest stable [Grafana](https://grafana.com/) release.

For convenience, there are also ansible roles for installation of yum
repositories with upstream releases of Ceph, Gluster and theirs installation
tools (such as `ceph-installer` and `gdeploy`):

* `tendrl-ansible.ceph-installer`
* `tendrl-ansible.gluster-gdeploy-copr`

Playbook files:

* `prechecks.yml`: playbook checking requirements before Tendrl installation
  (see comments inside the playbook file for references)
* `site.yml`: main playbook of tendrl-ansible, which one will use to install
  Tendrl


## Where are the roles and playbooks if I use rpm package?

Ansible roles are available in `/usr/share/ansible/roles/` directory, where
the role directories are prefixed with `tendrl-ansible.`, for example:
`/usr/share/ansible/roles/tendrl-ansible.tendrl-server`.
Each role has it's own `README.md` file, where you can find all details about
it's usage.

Playbooks are available in `/usr/share/doc/tendrl-ansible-1.6.0/` directory,
where `1.6.0` is version of tendrl-ansible package.


## What should I know before using tendrl-ansible?

You need to know [how to use
ansible](https://docs.ansible.com/ansible/latest/intro.html) and [how to deploy
and use ssh public
keys](https://docs.openshift.org/latest/install_config/install/host_preparation.html#ensuring-host-access)
(to be able to connect via ssh without asking for password).

Moreover since this README file can't provide all details about Tendrl, you
should read [Tendrl installation
documentation](https://github.com/Tendrl/documentation/wiki/Tendrl-release-latest)
as well.

And last but not least, both `tendrl-ansible.tendrl-server` and
`tendrl-ansible.tendrl-storage-node` roles contain
many variables which one can use to tweak the installation. See README files of
the roles for their description.


## What installation steps from Tendrl installation documentation are not part of tendrl-ansible?

This should be clear from [Tendrl installation
documentation](https://github.com/Tendrl/documentation/wiki/Tendrl-release-latest)
itself, but for the sake of convenience, here is the
list of installation or deployment steps which are out of scope of
tendrl-ansible:

* Deployment and installation of machines (either virtual or bare metal), which
  includes setup of networking, partitioning of disks, deployment of ssh public
  keys and so on.
* Installation and configuration of GlusterFS on the machines, see
  [gdeploy](https://gdeploy.readthedocs.io/en/latest/) for automation of this
  task.
* Setup of dedicated disk for etcd and graphite data directories.
* Setup of https for Tendrl web and api.
* Deployment of tls certificates and keys for etcd tls based client server
  encryption and authentication (this means communication between various
  tendrl components and etcd instance).


## How do I install Tendrl with tendrl-ansible?

1)  Install tendrl-ansible:

    ```
    # yum install tendrl-ansible
    ```

    See section "How to get tendrl-ansible?" in this README file for more
    details.

2)  Create [Ansible inventory
    file](https://docs.ansible.com/ansible/latest/intro_inventory.html) with
    groups for `tendrl_server` and `gluster_servers`. Here is an example of
    inventory file for 4 node cluster with Gluster:

    ```
    [gluster_servers]
    gl1.example.com
    gl2.example.com
    gl3.example.com
    gl4.example.com

    [tendrl_server]
    tendrl.example.com
    ```

3)  Add mandatory ansible variables into the inventory file you created in the
    previous step.

    This includes:

    * `etcd_ip_address` configures where etcd instance is listening
    * `etcd_fqdn` configure tendrl components to be able to connect to etcd
      instance
    * `graphite_fqdn` configures tendrl components to be able to connect to
      graphite instance (this value doesn't reconfigure graphite itself!)

    For simple example cluster from previous step, assuming there is only
    single network interface on all machines, the code you need to add into
    the inventory file would look like:

    ```
    [all:vars]
    etcd_ip_address=192.0.2.1
    etcd_fqdn=tendrl.example.com
    graphite_fqdn=tendrl.example.com
    ```

    Where `192.0.2.1` is ip address of tendrl server, `tendrl.example.com` is
    a hostname of tendrl server and `tendrl.example.com` hostname is translated
    to `192.0.2.1` ip address.

    See full description in README file of `tendrl-ansible.tendrl-server` role
    and pay attention
    to the values you specify there when you use multiple network interfaces
    on the machines.

    Note: you can define these variables anywhere else you like (eg. in
    variable files or from command line directly), but including them into the
    inventory provides you with a single file with almost full description of
    tendrl-ansible setup for future reference (eg. reruning tendrl-ansible
    later when you need to expand cluster or make sure the configuration still
    holds). The only information not stored in inventory file which you may
    need in the future is `grafana_admin_passwd` file, which contains grafana
    admin password, which will be generated during tendrl-ansible run.

4)  Add optional ansible variables into the inventory file.

    Based on Tendrl documentation and description in README files of
    tendrl-ansible roles, specify values for variables you like to tweak.

    This is important because some features tendrl-ansible can help you
    with are disabled by default as they require additional user input.

    This includes etcd tls client authentication (`etcd_tls_client_auth` and
    other variables), tendrl notifier configuration for snmp or smtp
    (`tendrl_notifier_email_id` and other variables), and other tweaks (eg.
    `tendrl_copr_repo` variable of `tendrl-ansible.tendrl-copr` role).

    There are also features such as firewalld setup for Tendrl (variable
    `configure_firewalld_for_tendrl`) which are enabled by default, but can be
    disabled if needed.

5)  If you use tendrl-ansible from rpm package, copy `site.yml` playbook into
    working directory (where you already store the inventory file):

    ```
    $ cp /usr/share/doc/tendrl-ansible-VERSION/site.yml .
    ```

    Do the same for prechecks playbook:

    ```
    $ cp /usr/share/doc/tendrl-ansible-VERSION/prechecks.yml .
    ```

6)  Check that ssh can connect to all machines from the inventory file without
    asking for password or validation of public key by running:

    ```
    $ ansible -i inventory_file -m ping all
    ```

    You should see ansible to show `"pong"` message for all machines.
    In case of any problems, you need to fix it before going on. If you are not
    sure what's wrong, consult documentation of ansible and/or ssh.

    The following example shows how to use [ansible become
    feature](https://docs.ansible.com/ansible/latest/become.html) **when direct
    ssh login of root user is not allowed** and you are connecting via non-root
    `cloud-user` account, which can leverage `sudo` to run any command as root
    without any password:

    ```
    $ ansible --become -u cloud-user -i inventory_file -m ping all
    ```

    If this is your case, you may consider converting command line arguments
    related to *Ansbile become feature* into [behavioral inventory
    parameters](https://docs.ansible.com/ansible/latest/intro_inventory.html#list-of-behavioral-inventory-parameters)
    and adding them into the inventory file. This way, you don't need to
    specify these arguments again for every ansible command. Example of this
    update which matches previous command line example follows (it should be
    appended to the `[all:vars]` section):

    ```
    ansible_become=yes
    ansible_user=cloud-user
    ```

    After this edit, you can re run the ping example without become command
    line arguments:

    ```
    $ ansible -i inventory_file -m ping all
    ```

7)  Now you can run prechecks playbook to verify if minimal requirements and
    setup for Tendrl are satisfied. Any problem with the pre checks will make
    the playbook run fail immediately, pointing you to a particular
    requirement or problem with configuration before the installation itself
    (preventing you to spend time with unnecessary debugging after
    installation).

    For **production deployment**, run the full check:

    ```
    $ ansible-playbook -i inventory_file prechecks.yml
    ```

    While for **proof of concept deployments**, you can avoid checking of
    stringent production requirements using `production` tag:

    ```
    $ ansible-playbook -i inventory_file prechecks.yml --skip-tags "production"
    ```

    If you are not sure why a particular check is there or what is checked
    exactly, open the playbook file and see comments and/or implementation of
    the check.

8)  Then we are ready to run ansible to install Tendrl:

    ```
    $ ansible-playbook -i inventory_file site.yml
    ```

    Assuming we have deployed ssh keys on the machines and have Gluster
    trusted storage pool already installed and running there.

9)  Log in to your tendrl server at ``http://tendrl.example.com`` (hostname
    of Tendrl server as specified in the inventory file in step #2)  with
    username ``admin`` and default password ``adminuser``.

    Note that `tendrl-ansible.tendrl-server` role includes setup of admin user
    account for
    Tendrl (usable with both api and web interface), and that default
    password is ``adminuser``. Moreover the admin password is also
    stored on *Tendrl Server* machine in `/root/password` file (this feature of
    tendrl-ansible is based
    on [TEN-257](https://tendrl.atlassian.net/browse/TEN-257)).


## How do I expand cluster with tendrl-ansible?

See [Tendrl wiki](https://github.com/Tendrl/documentation/wiki) for full
details of cluster expansion procedure. This section contains only brief
overview of the expand operation for you to understand how tendrl-ansible
fits into Tendrl cluster expand operation.

1)  First of all, you need to install operating system and Gluster on new
    servers(s) and add them into existing cluster (aka [Gluster *Trusted Storage
    Pool*](http://docs.gluster.org/en/latest/Administrator%20Guide/Storage%20Pools/))
    via peer probe and add bricks on new server(s) into existing gluster
    volume(s) based on your needs.

2)  When Gluster is aware of new servers (you see them in output of `gluster
    pool list` command), you add the new servers into ansible inventory file
    (into group `gluster_servers`) which you used during installation of
    Tendrl.

    Note that it's important to **add new servers into the same inventory file
    as was used during installation**, because you need to ensure that you are
    using the same set of ansible variables. For the same reason, you need to
    have the lookup file with password for grafana admin `grafana_admin_passwd`
    availabe in current directory.

3)  Then, you rerun ansible playbook in the same way as done during Tendrl
    installation:

    ```
    $ ansible-playbook -i inventory_file site.yml
    ```

    During this run, ansible should report "ok" status for
    already existing machines, while reporting "changed" status for the new
    machines you just added.

4)  Now, you should be able to see new servers in Tendrl web ui (see Tendrl
    documentation for details).


## License

Distributed under the terms of the [GNU LGPL, version
2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) license,
tendrl-ansible is free and open source software.
