%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname requests
%define srcname requests

Summary:       Requests is an Apache2 Licensed HTTP library, written in Python, for human beings 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       1.1.0
Release:       1%{?dist}
License:       ASL 2.0
Group:         Development/Languages
Source0:       http://pypi.python.org/packages/source/r/requests/requests-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 
%else
BuildRequires: 	python-setuptools
Requires:       python >= 2.5
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Most existing Python modules for sending HTTP requests are extremely verbose and cumbersome. Python's builtin urllib2 module provides most of the HTTP capabilities you should need, but the api is thoroughly broken. It requires an enormous amount of work (even method overrides) to perform the simplest of tasks.

%prep
%setup -q -n %{srcname}-%{version}
%{__rm} -rf tests

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{python_sitelib}/%{pkgname}/*
%{python_sitelib}/python_%{pkgname}-%{version}-py%{pyver}.egg-info

%changelog
