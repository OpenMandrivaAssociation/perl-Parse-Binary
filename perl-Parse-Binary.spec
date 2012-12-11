%define upstream_name    Parse-Binary
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Convert between variant records and hashes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module makes parsing binary data structures much easier, by serving as
a base class for classes that represents the binary data, which may contain
objects of other classes to represent parts of itself.

Documentation is unfortunately a bit lacking at this moment. Please read
the tests and source code of the Parse::AFP manpage and the Win32::Exe
manpage for examples of using this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 658872
- rebuild for updated spec-helper

* Sun May 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 381686
- import perl-Parse-Binary


* Sun May 31 2009 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist

