#
# Conditional build:
%bcond_without	python2 # Python 2.x module
%bcond_without	python3 # Python 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A comprehensive HTTP client library
Summary(pl.UTF-8):	Obszerna biblioteka klienta HTTP
Name:		python-httplib2
Version:	0.18.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://github.com/httplib2/httplib2/releases
Source0:	https://github.com/httplib2/httplib2/archive/v%{version}/httplib2-%{version}.tar.gz
# Source0-md5:	883f17828619757836ff510c42a7cca8
Patch0:		%{name}.certfile.patch
Patch1:		%{name}-0.9-proxy-http.patch
Patch2:		%{name}-mock.patch
URL:		https://github.com/httplib2/httplib2
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-future >= 0.16.0
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-pytest >= 3.2.1
BuildRequires:	python-pytest-cov >= 2.5.1
BuildRequires:	python-pytest-timeout >= 1.2.0
BuildRequires:	python-six >= 1.10.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.2.1
BuildRequires:	python3-pytest-cov >= 2.5.1
BuildRequires:	python3-pytest-timeout >= 1.2.0
BuildRequires:	python3-six >= 1.10.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
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
Requires:	ca-certificates

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
%patch2 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m pytest tests -k 'not test_certs_file_from_builtin and not test_certs_file_from_environment and not test_ipv6 and not test_with_certifi_removed_from_modules and not test_noproxy_star'
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
# in python3 implementation system socks module is preferred over httplib2.socks, and the first is incompatible with test_socks5_auth
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} -m pytest tests -k 'not test_certs_file_from_builtin and not test_certs_file_from_environment and not test_ipv6 and not test_with_certifi_removed_from_modules and not test_noproxy_star and not test_server_not_found_error_is_raised_for_invalid_hostname and not test_socks5_auth'
%endif
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/httplib2/cacerts.txt
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/httplib2/cacerts.txt
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%{py_sitescriptdir}/httplib2
%{py_sitescriptdir}/httplib2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-httplib2
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md python3/README
%{py3_sitescriptdir}/httplib2
%{py3_sitescriptdir}/httplib2-%{version}-py*.egg-info
%endif
