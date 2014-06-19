%define		status		stable
%define		pearname	Text_CAPTCHA_Numeral
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - generation of numeral maths captchas
Summary(pl.UTF-8):	%{pearname} - generowanie matematycznych captcha
Name:		php-pear-%{pearname}
Version:	1.3.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	16b98ca2d1af630120665808e704fae5
URL:		http://pear.php.net/package/Text_CAPTCHA_Numeral/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear >= 4:1.3-5
Obsoletes:	php-pear-Text_CAPTCHA_Numeral-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Numeral captcha generates mathematical operations and answers in order
to prove that bots using it are human.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Liczbowe captcha polega na generowania równań matecznych i rozwiązań
do nich w celu rozróżnienia między ludźmi a botami.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv docs/Text_CAPTCHA_Numeral/examples .
mv .%{php_pear_dir}/data/Text_CAPTCHA_Numeral/composer.json .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/CAPTCHA/Numeral.php
%{php_pear_dir}/Text/CAPTCHA/Numeral
%{_examplesdir}/%{name}-%{version}
