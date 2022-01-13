%global debug_package %{nil}
%{?!released_version: %global released_version 0.2.1}

Name:           task-core
Summary:        Python library for describing and resolving service dependencies
Version:        XXX
Release:        XXX

License:        ASL 2.0

URL:            https://github.com/Directord/task-core
Source:         https://github.com/Directord/task-core/archive/%{version}.tar.gz#/task-core-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-pbr >= 2.0.0

Recommends:     python3-%{name}
Recommends:     %{name}-examples

%description
Python library for describing and resolving service dependencies

%package -n python3-%{name}
Summary:        Python library code for task-core

Requires:       %{name} = %{version}-%{release}
# python requirements
Requires:       python3-jsonschema
Requires:       python3-networkx
Requires:       python3-stevedore
Requires:       python3-taskflow
Requires:       python3-yaml
# these are backends
Recommends:     directord
Recommends:     python3-ansible-runner

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python library code for task-core

%package -n %{name}-examples
Summary:        Example service and tasks for task-core

Requires:       %{name} = %{version}-%{release}

%description -n %{name}-examples
Example service and tasks for task-core

%prep
%autosetup -n task-core-* -S git
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
# TODO(mwhahaha): run tests

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/examples
%exclude %{_datadir}/%{name}/schema

%files -n python3-%{name}
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python3_sitelib}/task_core*
%{_bindir}/%{name}
%{_bindir}/task-core-example
%{_datadir}/%{name}/schema
%{_datadir}/%{name}/contrib

%files -n %{name}-examples
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{_datadir}/%{name}/examples

%changelog
