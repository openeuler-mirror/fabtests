Name:                fabtests
Version:             1.6.1
Release:             3
Summary:             libfabric API test suite
License:             BSD and (BSD or GPLv2) and MIT
Url:                 https://github.com/ofiwg/fabtests
Source:              https://github.com/ofiwg/fabtests/releases/download/v%{version}/fabtests-%{version}.tar.bz2
BuildRequires:       libfabric-devel >= %{version} valgrind-devel gcc
%description
Fabtests provides a set of examples that uses libfabric

%package             help
Summary:             documentation for fabtests
Requires:            fabtests = %{version}-%{release}

%description         help
Documentation for user of fabtests.

%prep
%autosetup -n fabtests-%{version} -p1 -S git

%build
%configure --with-valgrind
%make_build V=1

%install
%make_install
%delete_la

%files
%{_datadir}/fabtests/
%{_bindir}/*
%doc AUTHORS README COPYING

%files               help
%{_mandir}/man7/*

%changelog
* Tue Apr 21 2020 Jeffery.Gao <gaojianxing@huawei.com> - 1.6.1-3
- Package init