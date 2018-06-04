%define debug_package %{nil}
%define dracutlibdir %{_prefix}/lib/dracut

Name:           ignition
Version:        0.23.0
Release:        0.7%{?dist}
Summary:        First boot installer and configuration tool

License:        ASL 2.0
URL:            https://github.com/coreos/ignition 
Source0:        https://github.com/coreos/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/dustymabe/bootengine/archive/master.tar.gz

Patch0: 0001-build-Override-artifact-output-with-BIN_PATH.patch
Patch1: 0002-build_releases-Override-artifact-output-with-BIN_PAT.patch
Patch2: 0001-build-Allow-VERSION-set-and-fallback-to-git.patch
Patch3: 0002-build_releases-Allow-setting-VERSION-and-fallback-to.patch

BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang >= 1.6.2}
BuildRequires:  libblkid-devel
# See https://github.com/openshift/os/issues/59
#ExclusiveArch:  %{go_arches}

%description
Ignition is the utility used by CoreOS Container Linux to manipulate
disks during the initramfs. This includes partitioning disks,
formatting partitions, writing files (regular files, systemd units,
networkd units, etc.), and configuring users. On first boot, Ignition
reads its configuration from a source of truth (remote URL, network
metadata service, hypervisor bridge, etc.) and applies the
configuration.


%prep
# unpack source0 and apply patches
%autosetup -n %{name}-%{version}
# unpack source1 (dracut modules)
%setup -T -D -a 1 -n %{name}-%{version}


%build
# TODO: Using ./build_releases will output multiple archs. This could be used
#       to do multiple arch outputs in subpackages.
export VERSION=%{version}
# Tell ignition where to find chroot binary
export GLDFLAGS='-X github.com/coreos/ignition/internal/distro.chrootCmd=%{_sbindir}/chroot '
export BIN_PATH=./
./build

%install
# ignition
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./ignition %{buildroot}%{_bindir}
install -p -m 0755 ./ignition-validate %{buildroot}%{_bindir}
# dracut modules
install -d -p %{buildroot}/%{dracutlibdir}/modules.d
rm ./bootengine-master/dracut/README.txt
cp -r ./bootengine-master/dracut/* %{buildroot}/%{dracutlibdir}/modules.d/


%files
%license LICENSE
%doc README.md doc/
%{_bindir}/%{name}
%{_bindir}/%{name}-validate

%package dracut

Summary: The ignition dracut modules
Requires: ignition
Requires: dracut
Requires: dracut-network

%description dracut
Dracut modules for ignition to enable ignition services to run in the
initramfs on boot.

%files dracut
%defattr(-,root,root,0755)
%{dracutlibdir}/modules.d/30ignition
%{dracutlibdir}/modules.d/99journald-conf

%changelog
* Mon Jun 04 2018 Dusty Mabe <dusty@dustymabe.com> - 0.23.0-0.7
- dracut: usr-generator module was removed upstream
- dracut: journald-conf was added upstream

* Fri Jun 01 2018 Dusty Mabe <dusty@dustymabe.com> - 0.23.0-0.6
- Add ignition-dracut subpackage

* Thu May 31 2018 Dusty Mabe <dusty@dustymabe.com> - 0.23.0-0.5
- Tell ignition where to find chroot binary

* Thu May 10 2018 Steve Milner <smilner@redhat.com> - 0.23.0-0.4
- Update per review

* Mon Mar 26 2018 Dusty Mabe <dusty@dustymabe.com> - 0.23.0-0.3
- fixup spec so epel7 will build

* Tue Mar 20 2018 Dusty Mabe <dusty@dustymabe.com> - 0.23.0-0.2
- fixups for spec file

* Thu Mar 15 2018 Steve Milner <smilner@redhat.com> - 0.23.0-0.1
- Initial spec
