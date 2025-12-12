%global pypi_name build

Name:           python-%{pypi_name}
Version:        1.2.2.post1
Release:        3
Summary:        A simple, correct PEP517 package builder
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/build/
Source0:        https://files.pythonhosted.org/packages/source/b/build/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python
BuildSystem:	python

%description
Simple, correct PEP517 package builder.

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pyproject-build
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.dist-info
