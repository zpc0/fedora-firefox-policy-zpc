Name:		firefox-policy-zpc
Version:	0.1.0
Release:	%autorelease
Summary:	Firefox policies for zpc system

License:	GPL-3.0-or-later
URL:		https://zpc.st
Source0:	policies.json

BuildArch:	noarch

Requires:	firefox

%description
This is a enterprise policies file for
Mozilla Firefox

%prep

%build

%install
mkdir -p %{buildroot}%{_libdir}/firefox/distribution
install -m 0755 %{SOURCE0} %{buildroot}%{_libdir}/firefox/distribution/policies.json

%files
%license COPYING
%{_libdir}/firefox/distribution/policies.json

%changelog
%autochangelog
