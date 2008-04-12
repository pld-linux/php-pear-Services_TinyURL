%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	TinyURL
%define		_status		beta
%define		_pearname	Services_TinyURL
Summary:	%{_pearname} - PHP interface to TinyURL's API
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do API serwisu TinyURL
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	40cf7a8225ff55db877df9ac3f9f6cd1
URL:		http://pear.php.net/package/Services_TinyURL/
BuildRequires:	php-pear-PEAR-core
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for creating TinyURL's with their API as well as looking
up destinations of given TinyURL's.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs ten umożliwia tworzenie malutkich URL-i (TinyURL) z
wykorzystaniem API tego serwisu, jak również wyszukiwania adresów
docelowych już istniejących adresów TinyURL.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/TinyURL
%{php_pear_dir}/Services/TinyURL.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_TinyURL
