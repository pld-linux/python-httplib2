#
# Conditional build:
%bcond_without	python3 # Python 3.x module

Summary:	A comprehensive HTTP client library
Summary(pl.UTF-8):	Obszerna biblioteka klienta HTTP
Name:		python-httplib2
Version:	0.17.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/httplib2/httplib2/archive/v%{version}.tar.gz
# Source0-md5:	fbd0b80a32a4cbb1c3c459294e3a1065
Patch0:		%{name}.certfile.patch
Patch1:		%{name}-0.9-proxy-http.patch
URL:		https://github.com/httplib2/httplib2
BuildRequires:	python >= 2.3
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
Requires:	ca-certificates
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
%patch0 -p1
%patch1 -p1

%build
%py_build

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install
rm $RPM_BUILD_ROOT%{py_sitescriptdir}/httplib2/cacerts.txt

%if %{with python3}
%py3_install
rm $RPM_BUILD_ROOT%{py3_sitescriptdir}/httplib2/cacerts.txt
%endif

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG
%{py_sitescriptdir}/httplib2
%{py_sitescriptdir}/httplib2-%{version}-py*.egg-info

%if %{with python3}
%files -n python3-httplib2
%defattr(644,root,root,755)
%doc python3/README CHANGELOG
%{py3_sitescriptdir}/httplib2
%{py3_sitescriptdir}/httplib2-%{version}-py*.egg-info
%endif
