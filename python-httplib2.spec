#
# Conditional build:
%bcond_without	python3 # Python 3.x module

Summary:	A comprehensive HTTP client library
Summary(pl.UTF-8):	Obszerna biblioteka klienta HTTP
Name:		python-httplib2
Version:	0.8
Release:	3
License:	MIT
Group:		Development/Languages/Python
Source0:	http://httplib2.googlecode.com/files/httplib2-%{version}.zip
# Source0-md5:	0803da81fe1bb92f864715665defe65f
URL:		http://bitworking.org/projects/httplib2/
BuildRequires:	python >= 2.3
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A comprehensive HTTP client library, httplib2.py supports many
features left out of other HTTP libraries. Supports:
- HTTP and HTTPS
- Keep-Alive
- Authentication
- Caching
- All Methods
- Redirects
- Compression
- Lost update support
- Unit Tested

%description -l pl.UTF-8
httplib2.py to obszerna biblioteka klienta HTTP, obsługująca wiele
cech pomijanych przez inne biblioteki. Obsługuje:
- HTTP i HTTPS
- Keep-Alive
- uwierzytelnianie
- buforowanie
- wszystkie metody
- przekierowania
- kompresję
- Lost update
- podlega testom jednostkowym.

%package -n python3-httplib2
Summary:	A comprehensive HTTP client library
Summary(pl.UTF-8):	Obszerna biblioteka klienta HTTP
Group:		Development/Languages/Python

%description -n python3-httplib2
A comprehensive HTTP client library, httplib2.py supports many
features left out of other HTTP libraries. Supports:
- HTTP and HTTPS
- Keep-Alive
- Authentication
- Caching
- All Methods
- Redirects
- Compression
- Lost update support
- Unit Tested

%description -n python3-httplib2 -l pl.UTF-8
httplib2.py to obszerna biblioteka klienta HTTP, obsługująca wiele
cech pomijanych przez inne biblioteki. Obsługuje:
- HTTP i HTTPS
- Keep-Alive
- uwierzytelnianie
- buforowanie
- wszystkie metody
- przekierowania
- kompresję
- Lost update
- podlega testom jednostkowym.

%prep
%setup -q -n httplib2-%{version}

%if %{with python3}
rm -rf build-3
set -- *
install -d build-3
cp -a "$@" build-3
find build-3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%if %{with python3}
cd build-3
%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
cd ..
%endif

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%{py_sitescriptdir}/httplib2
%{py_sitescriptdir}/httplib2-%{version}-py*.egg-info

%files -n python3-httplib2
%defattr(644,root,root,755)
%doc python3/README CHANGELOG
%{py3_sitescriptdir}/httplib2
%{py3_sitescriptdir}/httplib2-%{version}-py*.egg-info
