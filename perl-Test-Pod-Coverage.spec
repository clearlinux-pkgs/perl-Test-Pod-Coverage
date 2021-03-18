#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Pod-Coverage
Version  : 1.10
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-1.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-1.10.tar.gz
Summary  : 'Check for pod coverage in your distribution'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Test-Pod-Coverage-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::Symdump)
BuildRequires : perl(Pod::Coverage)

%description
This module is used to add a test to your Perl distribution,
which checks for pod coverage of all appropriate files.

%package dev
Summary: dev components for the perl-Test-Pod-Coverage package.
Group: Development
Provides: perl-Test-Pod-Coverage-devel = %{version}-%{release}
Requires: perl-Test-Pod-Coverage = %{version}-%{release}

%description dev
dev components for the perl-Test-Pod-Coverage package.


%package perl
Summary: perl components for the perl-Test-Pod-Coverage package.
Group: Default
Requires: perl-Test-Pod-Coverage = %{version}-%{release}

%description perl
perl components for the perl-Test-Pod-Coverage package.


%prep
%setup -q -n Test-Pod-Coverage-1.10
cd %{_builddir}/Test-Pod-Coverage-1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Pod::Coverage.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Test/Pod/Coverage.pm
