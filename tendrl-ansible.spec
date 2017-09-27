# This rpm spec file is based on packaging approach used by linux-system-roles
# project, as there are no Fedora packaging guidelines for ansible or better
# examples to follow. Target OS is RHEL or CentOS 7.

Name:           tendrl-ansible
Version:        1.5.3
Release:        1%{?dist}
Summary:        Ansible roles and playbooks for Tendrl

License:        LGPLv2.1
Url:            https://github.com/Tendrl/tendrl-ansible
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       ansible
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
# reference roles by prefixed name in sample playbook file
sed -i 's/- \(ceph-installer\)/- %{roleprefix}\1/g' site.yml.sample
sed -i 's/- \(gluster-gdeploy-copr\)/- %{roleprefix}\1/g' site.yml.sample
sed -i 's/- \(grafana-repo\)/- %{roleprefix}\1/g' site.yml.sample
sed -i 's/- \(tendrl-copr\)/- %{roleprefix}\1/g' site.yml.sample
sed -i 's/- \(tendrl-server\)/- %{roleprefix}\1/g' site.yml.sample
sed -i 's/- \(tendrl-storage-node\)/- %{roleprefix}\1/g' site.yml.sample

# reference playbooks by full paths in sample playbook file
sed -i 's!prechecks.yml!%{_pkgdocdir}/&!g'                   site.yml.sample
sed -i 's!workaround.disable-firewall.yml!%{_pkgdocdir}/&!g' site.yml.sample
sed -i 's!workaround.disable-selinux.yml!%{_pkgdocdir}/&!g'  site.yml.sample

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles

# install ansible roles
cp -pR roles/ceph-installer         $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}ceph-installer
cp -pR roles/gluster-gdeploy-copr   $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}gluster-gdeploy-copr
cp -pR roles/grafana-repo           $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}grafana-repo
cp -pR roles/tendrl-copr            $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}tendrl-copr
cp -pR roles/tendrl-server          $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}tendrl-server
cp -pR roles/tendrl-storage-node    $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}tendrl-storage-node

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/

# install playbooks
install -p -m 644 site.yml.sample                    $RPM_BUILD_ROOT%{_pkgdocdir}/site.yml.sample
install -p -m 644 prechecks.yml                      $RPM_BUILD_ROOT%{_pkgdocdir}/prechecks.yml
install -p -m 644 workaround.disable-firewall.yml    $RPM_BUILD_ROOT%{_pkgdocdir}/workaround.disable-firewall.yml
install -p -m 644 workaround.disable-selinux.yml     $RPM_BUILD_ROOT%{_pkgdocdir}/workaround.disable-selinux.yml

# install readme and license files
install -p -m 644 README.rpm.md                $RPM_BUILD_ROOT%{_pkgdocdir}/README.md
install -p -m 644 LICENSE                      $RPM_BUILD_ROOT%{_pkgdocdir}/LICENSE

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
%doc %{_pkgdocdir}/site.yml.sample

# playbooks (referenced in site.yml.sample) in doc dir (temporary HACK)
%doc %{_pkgdocdir}/prechecks.yml
%doc %{_pkgdocdir}/workaround.disable-firewall.yml
%doc %{_pkgdocdir}/workaround.disable-selinux.yml

# readme and license files
%doc %{_pkgdocdir}/README.md
%license %{_pkgdocdir}/LICENSE

%changelog
* Wed Sep 27 2017  Martin Bukatovič <mbukatov@redhat.com> - 1.5.3-1
- First release with tendrl-ansible provided in rpm package.
- Initial specfile based on rhel-system-roles packaging style.

