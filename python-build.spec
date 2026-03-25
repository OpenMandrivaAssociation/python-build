%global module build

Name:           python-build
Version:        1.4.2
Release:        1
Summary:        A simple, correct PEP517 package builder
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/build/
Source0:        https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
A simple, correct PEP517 package builder.

See the documentation for more info: https://build.pypa.io/

%files
%doc README.md
%license LICENSE
%{_bindir}/pyproject-build
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
