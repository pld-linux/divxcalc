Summary:	A bitrate calculator for DivX:-) movies
Summary(pl):	Kalkulator bitrate dla filmów DivX:-)
Name:		divxcalc
Version:	0.4a
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://axljab.homelinux.org:8080/software/divxcalc/%{name}-%{version}.tar.gz
URL:		http://axljab.homelinux.org:8080/?m=sw&p=divxcalc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DivX Calc is a simple DivX calculator for Linux. It uses a simple GTK
interface which calculates which bitrate to use while encoding a movie
using DivX ;-).

%description -l pl
DivX Calc to prosty kalkulator DivX dla Linuksa. Za pomoc± prostego 
interfejsu GTK mo¿na przeliczyæ jaki bitrate zastosowaæ do kompresji
filmu za pomoc± DivX ;-).

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
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
