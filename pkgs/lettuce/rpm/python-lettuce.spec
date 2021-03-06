%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %global pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
%define pkgname lettuce
%define srcname lettuce

Summary:       Behaviour Driven Development for python 
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:          python26-%{pkgname}
%else
Name:          python-%{pkgname}
%endif

Version:       0.2.16
Release:       1%{?dist}
License:       GPL 3.0
Group:         Development/Languages
Source0:       http://pypi.python.org/packages/source/l/lettuce/lettuce-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26 ipython >= 0.1 python26-sure python26-fuzzywuzzy python26-ipdb
%else
Requires:       python >= 2.5 ipython >= 0.1 python-sure python-fuzzywuzzy python-ipdb
%endif
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Behaviour Driven Development for python

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
%{python_sitelib}/%{srcname}/*
%{python_sitelib}/%{srcname}-%{version}-py%{pyver}.egg-info
/usr/bin/

%changelog

