%define debug_package %{nil}

Name:           ignition
Version:        0.23.0
Release:        0.2%{?dist}
Summary:        First boot installer and configuration tool

License:        ASLv2
URL:            https://github.com/coreos/ignition 
Source0:        https://github.com/coreos/%{name}/archive/v%{version}.tar.gz

Patch0: 0001-build-Override-artifact-output-with-BIN_PATH.patch
Patch1: 0002-build_releases-Override-artifact-output-with-BIN_PAT.patch
Patch2: 0001-build-Allow-VERSION-set-and-fallback-to-git.patch
Patch3: 0002-build_releases-Allow-setting-VERSION-and-fallback-to.patch

BuildRequires:  golang
BuildRequires:  go-compilers-golang-compiler
BuildRequires:  libblkid-devel

%description
Ignition is the utility used by CoreOS Container Linux to manipulate
disks during the initramfs. This includes partitioning disks,
formatting partitions, writing files (regular files, systemd units,
networkd units, etc.), and configuring users. On first boot, Ignition
reads its configuration from a source of truth (remote URL, network
metadata service, hypervisor bridge, etc.) and applies the
configuration.


%prep
%autosetup -n %{name}-%{version}


%build
# TODO: Using ./build_releases will output multiple archs. This could be used
#       to do multiple arch outputs in subpackages.
VERSION=%{version} BIN_PATH=./ ./build

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./ignition %{buildroot}%{_bindir}
install -p -m 0755 ./ignition-validate %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md doc/
%{_bindir}/%{name}
%{_bindir}/%{name}-validate


%changelog
* Tue Mar 20 2018 Dusty Mabe <dusty@dustymabe.com> - 0.23.0-0.2
- fixups for spec file

* Thu Mar 15 2018 Steve Milner <smilner@redhat.com> - 0.23.0-0.1
- Initial spec
- 
