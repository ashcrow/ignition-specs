%define debug_package %{nil}
%define dracutlibdir %{_prefix}/lib/dracut

Name:     dracut-bootengine
Version:  0.0.1
Release:  0.1%{?dist}
Summary:  Bootengine dracut modules for Container Linux
Group:    System Environment/Base
License:  BSD
URL:      https://github.com/coreos/bootengine
Source0:  dracut-bootengine-%{version}.tar.gz
Provides: dracut-bootengine = %{version}-%{release}
BuildArch: noarch

Requires: ignition
Requires: dracut
Requires: bash >= 4
Requires: coreutils
Requires: filesystem >= 2.1.0
Requires: findutils
Requires: grep
Requires: sed

%description
bootengine dracut modules for Container Linux.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/
cp -rf dracut/* $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/


%files
%defattr(-,root,root,0755)
%doc README.md NOTICE
%license LICENSE
%{dracutlibdir}/modules.d/03coreos-network/10-nodeps.conf
%{dracutlibdir}/modules.d/03coreos-network/module-setup.sh
%{dracutlibdir}/modules.d/03coreos-network/network-cleanup.service
%{dracutlibdir}/modules.d/03coreos-network/parse-ip-for-networkd.sh
%{dracutlibdir}/modules.d/03coreos-network/yy-azure-sriov.network
%{dracutlibdir}/modules.d/03coreos-network/yy-digitalocean.network
%{dracutlibdir}/modules.d/03coreos-network/yy-oracle-oci.network
%{dracutlibdir}/modules.d/03coreos-network/yy-pxe.network
%{dracutlibdir}/modules.d/03coreos-network/zz-default.network
%{dracutlibdir}/modules.d/10diskless-generator/diskless-btrfs
%{dracutlibdir}/modules.d/10diskless-generator/diskless-generator
%{dracutlibdir}/modules.d/10diskless-generator/module-setup.sh
%{dracutlibdir}/modules.d/10usr-fsck-generator/module-setup.sh
%{dracutlibdir}/modules.d/10usr-fsck-generator/testsuite.sh
%{dracutlibdir}/modules.d/10usr-fsck-generator/usr-fsck-generator
%{dracutlibdir}/modules.d/10usr-generator/module-setup.sh
%{dracutlibdir}/modules.d/10usr-generator/remount-sysroot.service
%{dracutlibdir}/modules.d/10usr-generator/testsuite.sh
%{dracutlibdir}/modules.d/10usr-generator/usr-generator
%{dracutlibdir}/modules.d/10verity-generator/README
%{dracutlibdir}/modules.d/10verity-generator/module-setup.sh
%{dracutlibdir}/modules.d/10verity-generator/no-job-timeout.conf
%{dracutlibdir}/modules.d/10verity-generator/verity-generator
%{dracutlibdir}/modules.d/30disk-uuid/90-disk-uuid.rules
%{dracutlibdir}/modules.d/30disk-uuid/disk-uuid@.service
%{dracutlibdir}/modules.d/30disk-uuid/module-setup.sh
%{dracutlibdir}/modules.d/30ignition/coreos-digitalocean-network.service
%{dracutlibdir}/modules.d/30ignition/coreos-static-network.service
%{dracutlibdir}/modules.d/30ignition/ignition-disks.service
%{dracutlibdir}/modules.d/30ignition/ignition-files.service
%{dracutlibdir}/modules.d/30ignition/ignition-generator
%{dracutlibdir}/modules.d/30ignition/ignition-quench.service
%{dracutlibdir}/modules.d/30ignition/ignition-setup.sh
%{dracutlibdir}/modules.d/30ignition/module-setup.sh
%{dracutlibdir}/modules.d/30ignition/retry-umount.sh
%{dracutlibdir}/modules.d/30ignition/sysroot-boot.service
%{dracutlibdir}/modules.d/50ca-certs/module-setup.sh
%{dracutlibdir}/modules.d/80disable-net-names/module-setup.sh
%{dracutlibdir}/modules.d/90iscsi-root/iscsi-root-generator
%{dracutlibdir}/modules.d/90iscsi-root/module-setup.sh
%{dracutlibdir}/modules.d/90iscsi-root/oracle-oci-root.service
%{dracutlibdir}/modules.d/99dracut-root/module-setup.sh
%{dracutlibdir}/modules.d/99dracut-root/parse-stub.sh
%{dracutlibdir}/modules.d/99emergency-timeout/module-setup.sh
%{dracutlibdir}/modules.d/99emergency-timeout/timeout.sh
%{dracutlibdir}/modules.d/99journald-conf/00-forward-to-console.conf
%{dracutlibdir}/modules.d/99journald-conf/module-setup.sh
%{dracutlibdir}/modules.d/99setup-root/initrd-setup-root
%{dracutlibdir}/modules.d/99setup-root/initrd-setup-root.service
%{dracutlibdir}/modules.d/99setup-root/module-setup.sh
%{dracutlibdir}/modules.d/99shadow/module-setup.sh
%{dracutlibdir}/modules.d/99start-root/65-start-root.rules
%{dracutlibdir}/modules.d/99start-root/module-setup.sh

%changelog
* Fri Mar 16 2018 Steve Milner <smilner@redhat.com> - 0.0.1-0.1
- Initial spec
