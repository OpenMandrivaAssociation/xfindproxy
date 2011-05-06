Name: xfindproxy
Version: 1.0.2
Release: %mkrel 2
Summary: Locate proxy services
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libice-devel >= 1.0.0
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
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
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfindproxy
%{_mandir}/man1/xfindproxy.1*
