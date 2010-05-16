#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	App
%define	pnam	SVN-Bisect
Summary:	App::SVN::Bisect - binary search through svn revisions
Name:		perl-App-SVN-Bisect
Version:	1.0
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/App/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8540f354b27d904eee56cc473542cbc
Patch0:		%{name}-locale.patch
URL:		http://search.cpan.org/dist/App-SVN-Bisect/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::All) > 0.38
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Output
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-YAML-Syck
BuildRequires:	subversion
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the backend of the "svn-bisect" command line
tool. See the POD documentation of that tool, for usage details.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/svn-bisect
%{perl_vendorlib}/App/SVN/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
