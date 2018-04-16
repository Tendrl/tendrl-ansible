# This rpm spec file is based on packaging approach used by linux-system-roles
# project, as there are no Fedora packaging guidelines for ansible or better
# examples to follow. Target OS is RHEL or CentOS 7.

Name:           tendrl-ansible
Version:        1.6.3
Release:        1%{?dist}
Summary:        Ansible roles and playbooks for Tendrl

License:        LGPLv2.1
Url:            https://github.com/Tendrl/tendrl-ansible
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       ansible >= 2.4
Requires:       python-dns
BuildRequires:  yamllint

# All ansible roles from tendrl-ansible will have this prefix added into the
# name of the role (name of the directory with the role) to prevent conflicts.
%global roleprefix %{name}.

%description
Ansible roles and playbooks for installation of Tendrl, based on upstream
Tendrl documentation.


%prep
%setup -q

%build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles

# install ansible roles
cp -pR roles/tendrl-ansible.ceph-installer         $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ceph-installer
cp -pR roles/tendrl-ansible.gluster-gdeploy-copr   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}gluster-gdeploy-copr
cp -pR roles/tendrl-ansible.grafana-repo           $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}grafana-repo
cp -pR roles/tendrl-ansible.tendrl-copr            $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}tendrl-copr
cp -pR roles/tendrl-ansible.tendrl-server          $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}tendrl-server
cp -pR roles/tendrl-ansible.tendrl-storage-node    $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}tendrl-storage-node

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/

# install playbooks
install -p -m 644 site.yml                     $RPM_BUILD_ROOT%{_pkgdocdir}/site.yml
install -p -m 644 prechecks.yml                $RPM_BUILD_ROOT%{_pkgdocdir}/prechecks.yml

# install readme, license and example files
install -p -m 644 README.md                    $RPM_BUILD_ROOT%{_pkgdocdir}/README.md
install -p -m 644 LICENSE                      $RPM_BUILD_ROOT%{_pkgdocdir}/LICENSE
install -p -m 644 hosts.example                $RPM_BUILD_ROOT%{_pkgdocdir}/hosts.example

%check
yamlint $RPM_BUILD_ROOT && rm .yamlint

%files
%{_datadir}/ansible/roles/%{roleprefix}ceph-installer
%{_datadir}/ansible/roles/%{roleprefix}gluster-gdeploy-copr
%{_datadir}/ansible/roles/%{roleprefix}grafana-repo
%{_datadir}/ansible/roles/%{roleprefix}tendrl-copr
%{_datadir}/ansible/roles/%{roleprefix}tendrl-server
%{_datadir}/ansible/roles/%{roleprefix}tendrl-storage-node

# mark readme files in ansible roles as documentation
%doc %{_datadir}/ansible/roles/%{roleprefix}ceph-installer/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}gluster-gdeploy-copr/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}grafana-repo/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}tendrl-copr/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}tendrl-server/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}tendrl-storage-node/README.md

# mark example site.yml file as documentation
%doc %{_pkgdocdir}/site.yml

# playbooks (referenced in site.yml) in doc dir (temporary HACK)
%doc %{_pkgdocdir}/prechecks.yml

# example of ansible inventory file for tendrl-ansible
%doc %{_pkgdocdir}/hosts.example

# readme and license files
%doc %{_pkgdocdir}/README.md
%license %{_pkgdocdir}/LICENSE

%changelog
* Mon Apr 16 2018  Martin Bukatovič <mbukatov@redhat.com> - 1.6.3-1
- New build for upstream Tendrl v1.6.3

* Tue Mar 27 2018  Martin Bukatovič <mbukatov@redhat.com> - 1.6.2-1
- New build for upstream Tendrl v1.6.2

* Thu Mar  8 2018  Martin Bukatovič <mbukatov@redhat.com> - 1.6.1-1
- New build for upstream Tendrl rc v1.6.1 (milestone-3 2018)

* Fri Feb 16 2018  Martin Bukatovič <mbukatov@redhat.com> - 1.5.5-1
- New build for upstream Tendrl rc build 1.5.5

* Thu Nov 2 2017  Martin Bukatovič <mbukatov@redhat.com> - 1.5.4-1
- New build for upstream Tendrl release 1.5.4
- Add SELinux setup https://github.com/Tendrl/tendrl-ansible/issues/44
- Fix bug https://github.com/Tendrl/tendrl-ansible/issues/56
- Fix bug https://github.com/Tendrl/tendrl-ansible/issues/58
- Add SNMP setup https://github.com/Tendrl/tendrl-ansible/issues/59

* Fri Oct 6 2017  Martin Bukatovič <mbukatov@redhat.com> - 1.5.3-2
- Update requires to make it clear that we need ansible >= 2.3

* Wed Sep 27 2017  Martin Bukatovič <mbukatov@redhat.com> - 1.5.3-1
- First release with tendrl-ansible provided in rpm package.
- Initial specfile based on rhel-system-roles packaging style.

