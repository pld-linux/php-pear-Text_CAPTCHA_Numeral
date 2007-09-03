%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	CAPTCHA_Numeral
%define		_status		stable
%define		_pearname	Text_CAPTCHA_Numeral
Summary:	%{_pearname} - generation of numeral maths captchas
Summary(pl.UTF-8):	%{_pearname} - generowanie matematycznych captcha
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	0.1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0a1b4b4aac1b9e2bd0246f62748154fa
URL:		http://pear.php.net/package/Text_CAPTCHA_Numeral/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Numeral captcha generates mathematical operations and answers in order
to prove that bots using it are human.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Liczbowe captcha polega na generowania równań matecznych i rozwiązań
do nich w celu rozróżnienia między ludźmi a botami.

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
%doc install.log docs/Text_CAPTCHA_Numeral/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/interfaces/NumeralInterface.php
%{php_pear_dir}/Numeral.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Text_CAPTCHA_Numeral
%endif
