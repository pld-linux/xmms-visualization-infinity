Summary:	Infinity visualization plugin
Summary(pl):	Wtyczka wizualizacji infinity
Name:		xmms-visualization-infinity
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://julien.carme.free.fr/infinity-%{version}.tar.gz
URL:		http://julien.carme.free.fr/infinite.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Infinity visualization plugin.

%description -l pl
Wtyczka wizualizacji infinity.

%prep
%setup -q -n infinity-%{version}

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%{_datadir}/xmms/*
