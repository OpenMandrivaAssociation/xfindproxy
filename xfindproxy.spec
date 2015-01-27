Name: xfindproxy
Version: 1.0.3
Release: 1
Summary: Locate proxy services
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(ice) >= 1.0.0
BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
xfindproxy is a program used to locate available proxy services.
It utilizes the Proxy Management Protocol to communicate with a proxy
manager. The proxy manager keeps track of all available proxy services,
starts new proxies when necessary, and makes sure that proxies are shared
whenever possible.

%prep
%setup -q -n %{name}-%{version}

%build
%configure

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/xfindproxy
%{_mandir}/man1/xfindproxy.1*
