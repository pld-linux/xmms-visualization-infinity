Summary:	Infinity visualization plugin
Name:		xmms-visualization-infinity
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://julien.carme.free.fr/infinity-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://julien.carme.free.fr/infinite.html
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Infinity visualization plugin.

%description -l pl
Plugin wizualizacji infinity.

%prep
%setup -q -n infinity-%{version}
%patch0 -p1

%build
rm missing
automake -a -c -i
aclocal
autoconf
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
