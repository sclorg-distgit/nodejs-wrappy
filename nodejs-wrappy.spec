%{?scl:%scl_package nodejs-wrappy}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}nodejs-wrappy
Version:        1.0.1
Release:        3%{?dist}
Summary:        Callback wrapping utility
License:        ISC
Group:          Development/Languages/Other
Url:            https://github.com/npm/wrappy
Source:         http://registry.npmjs.org/wrappy/-/wrappy-%{version}.tgz
BuildRequires:  %{scl}
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%nodejs_find_provides_and_requires

%description
Callback wrapping utility

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/wrappy
cp -pr package.json wrappy.js \
        %{buildroot}%{nodejs_sitelib}/wrappy/

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{nodejs_sitelib}/wrappy

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- rebuilt

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
-  Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build

