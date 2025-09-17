#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A comprehensive HTTP client library
Summary(pl.UTF-8):	Obszerna biblioteka klienta HTTP
Name:		python-httplib2
Version:	0.22.0
Release:	4
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://github.com/httplib2/httplib2/releases
Source0:	https://github.com/httplib2/httplib2/archive/v%{version}/httplib2-%{version}.tar.gz
# Source0-md5:	e1ea1cd44c908a78112b6007af0f5917
Patch0:		%{name}.certfile.patch
Patch1:		%{name}-0.9-proxy-http.patch
URL:		https://github.com/httplib2/httplib2
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-future >= 0.16.0
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-pyparsing >= 2.4.2
BuildRequires:	python-pyparsing < 3
BuildRequires:	python-pytest >= 4.6.11
BuildRequires:	python-pytest-cov >= 2.5.1
BuildRequires:	python-pytest-forked >= 1.3.0
# >= 2.12.1
BuildRequires:	python-pytest-randomly >= 1.2.3
BuildRequires:	python-pytest-timeout >= 1.4.2
BuildRequires:	python-six >= 1.10.0
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

%prep
%setup -q -n httplib2-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin,pytest_timeout \
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m pytest tests -k 'not test_certs_file_from_builtin and not test_certs_file_from_environment and not test_ipv6 and not test_with_certifi_removed_from_modules and not test_noproxy_star'
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/httplib2/cacerts.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%{py_sitescriptdir}/httplib2
%{py_sitescriptdir}/httplib2-%{version}-py*.egg-info
