%global pypi_name build

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1
Summary:        A simple, correct PEP517 package builder
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/build/
Source0:        https://files.pythonhosted.org/packages/source/b/build/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python%{py_ver}dist(setuptools)
BuildRequires:  python%{py_ver}dist(packaging)
BuildRequires:  python%{py_ver}dist(pep517)

%description
Simple, correct PEP517 package builder.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pyproject-build
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
