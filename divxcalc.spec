Summary:	A bitrate calculator for DivX ;-) movies
Summary(pl.UTF-8):	Kalkulator bitrate dla filmów DivX ;-)
Name:		divxcalc
Version:	0.4a
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://axljab.homelinux.org:8080/software/divxcalc/%{name}-%{version}.tar.gz
# Source0-md5:	c51ed74b3c8693d9185ce31d0e23915d
URL:		http://axljab.homelinux.org:8080/?m=sw&p=divxcalc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DivX Calc is a simple DivX calculator for Linux. It uses a simple GTK+
interface which calculates which bitrate to use while encoding a movie
using DivX ;-).

%description -l pl.UTF-8
DivX Calc to prosty kalkulator DivX dla Linuksa. Za pomocą prostego
interfejsu GTK+ można przeliczyć jaki bitrate zastosować do kompresji
filmu za pomocą DivX ;-).

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
