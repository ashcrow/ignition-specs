%define debug_package %{nil}

Name:           ignition
Version:        0.23.0
Release:        0.1%{?dist}
Summary:        First boot installer and configuration tool

License:        ASLv2
URL:            https://github.com/coreos/ignition 
Source0:        https://github.com/coreos/%{name}/archive/v%{version}.tar.gz

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
%autosetup -n v%{version}


%build
# Build and install are done in the same script

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
# TODO: Using ./build_releases will output multiple archs. This could be used
#       to do multiple arch outputs in subpackages.
VERSION=%{version} BIN_PATH=$RPM_BUILD_ROOT/%{_bindir} ./build

%files
%license LICENSE
%doc README.md doc/
%{_bindir}/%{name}
%{_bindir}/%{name}-validate


%changelog
* Thu Mar 15 2018 Steve Milner <smilner@redhat.com> - 0.23.0-0.1
- Initial spec
- 
