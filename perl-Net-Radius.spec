%define		real_name Net-Radius
Name:		perl-%{real_name}
Version:	2.103
Release:	1%{?dist}
Summary:	Object-oriented Perl interface to RADIUS

Group:          Development/Libraries
License:        Artistic/GPL
URL:            http://search.cpan.org/dist/Net-Radius/
Source0:        http://search.cpan.org/CPAN/authors/id/L/LU/LUISMUNOZ/Net-Radius-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Warn)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Object-oriented Perl interface to RADIUS.


%prep
%setup -q -n %{real_name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.3COM README.VSA README.broken README.packets README.server contrib/ docs/ examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Tue Aug 28 2012 Olivier Bilodeau <olivier@bottomlesspit.org> - 2.103-1
- Initial release.
