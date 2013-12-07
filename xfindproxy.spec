Name: xfindproxy
Version: 1.0.2
Release: 8
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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 671310
- mass rebuild

* Tue Jan 11 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1
+ Revision: 630937
- Fix file list
- Remove redundant configure arguments

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2011.0
+ Revision: 608205
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2010.1
+ Revision: 524441
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351155
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226036
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154752
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 68895
- clean spec, add description


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

