Summary:	Infinity visualization plugin
Summary(pl):	Wtyczka wizualizacji infinity
Name:		xmms-visualization-infinity
Version:	0.2
Release:	4
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://julien.carme.free.fr/infinity-%{version}.tar.gz
# Source0-md5:	ec1400a7eb62cd674e25003e04cb232b
URL:		http://julien.carme.free.fr/infinite.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --visualization-plugin-dir)
%define		_xmms_data_dir		%(xmms-config --data-dir)

%description
Infinity visualization plugin.

%description -l pl
Wtyczka wizualizacji infinity.

%prep
%setup -q -n infinity-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_xmms_plugin_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
%{_xmms_data_dir}/*
