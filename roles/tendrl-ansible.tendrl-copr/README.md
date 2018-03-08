Tendrl Copr
===========

Enable official upstream yum repositories with latest stable
[Tendrl](http://tendrl.org/) relese, which are maintained in
[Copr](https://docs.pagure.org/copr.copr/user_documentation.html#faq):

* [tendrl-release](https://copr.fedorainfracloud.org/coprs/tendrl/release/)
* [tendrl-dependencies](https://copr.fedorainfracloud.org/coprs/tendrl/dependencies/).

Based on [Tendrl Package Installation
Reference](https://github.com/Tendrl/documentation/wiki/Tendrl-Package-Installation-Reference).

Requirements
------------

Expected operating system is *CentOS 7*, with both *CentOS-7 - Base* and
*CentOS-7 - Extras* repositories enabled (extras is required for `epel-release`
rpm package).

Role Variables
--------------

* When `tendrl_copr_repo` variable is set to `master`, this role will use
  [copr repository with latest devel snapshot
  builds](https://copr.fedorainfracloud.org/coprs/tendrl/tendrl/) instead of
  latest release, which would be otherwise used by default (as listed above).
  Note that switching to `master` is not supported and intended for testing and
  development purposes only.

License
-------

GNU Lesser General Public License, version 2.1
