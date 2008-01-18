Name: xfindproxy
Version: 1.0.1
Release: %mkrel 5
Summary: Locate proxy services
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libice-devel	>= 1.0.4
BuildRequires: libxt-devel	>= 1.0.5

%description
xfindproxy is a program used to locate available proxy services.
It utilizes the Proxy Management Protocol to communicate with a proxy
manager. The proxy manager keeps track of all available proxy services,
starts new proxies when necessary, and makes sure that proxies are shared
whenever possible.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfindproxy
%{_mandir}/man1/xfindproxy.1x*
