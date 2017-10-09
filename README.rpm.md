tendrl-ansible
==============

Ansible roles and playbooks for [Tendrl](http://tendrl.org/)!


## What does it do?

There are ansible roles for installation of [Tendrl](http://tendrl.org/), based
on upstream Tendrl documentation. You should check this documentation to have
basic understanding of various machine roles in Tendrl cluster before using
tendrl-ansible.

To list all available roles, see directories prefixed with `tendrl-ansible.`
in `/usr/share/ansible/roles/`. Each role has it's own `README.md` file, where
you can find all details about it's usage.

To understand how all this fits together, see sample ansible playbook file
`/usr/share/doc/tendrl-ansible-VERSION/site.yml.sample`.

Also note that the sample playbook includes
`/usr/share/doc/tendrl-ansible-VERSION/prechecks.yml`, which you can run
directly as well to check if minimal requirements and setup for Tendrl are
satisfied. Any problem with the pre checks will make sample site.yml file
immediately fail, pointing you to a particular requirement or problem with
configuration before the installation itself (preventing you to spare time
with unnecessary debugging after installation).

## Basic setup

1)  Install tendrl-ansible:

    ```
    # yum install tendrl-ansible
    ```

2)  Create Ansible inventory file with groups for `tendrl-server`
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

3)  Create `site.yml` file based on `site.yml.sample` and make sure to
    define all ansible variables in the playbook to suit:

    ```
    $ cp /usr/share/doc/tendrl-ansible-VERSION/site.yml.sample site.yml
    $ vim site.yml
    ```

4)  Check that ssh can connect to all machines from the inventory file without
    asking for password or validation of public key by running:

    ```
    $ ansible -i inventory_file -m ping all
    ```

    You should see ansible to show `"pong"` message for all machines.
    In case of any problems, you need to fix it before going on. If you are not
    sure what's wrong, consult documentation of ansible and/or ssh.

5)  Then we are ready to run ansible to install Tendrl:

    ```
    $ ansible-playbook -i inventory_file site.yml
    ```

    Assuming we have deployed ssh keys on the machines and have a cluster
    already installed and running there.

6)  Log in to your tendrl server at ``http://ip.of.tendrl.server`` with
    ``admin`` user and the default password ``adminuser``.


## License

Distributed under the terms of the [GNU LGPL, version
2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html) license,
tendrl-ansible is free and open source software.
