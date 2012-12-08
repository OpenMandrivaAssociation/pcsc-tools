%define name pcsc-tools
%define version 1.4.20

%define num_release 1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Summary:	PCSC tools useful for a PC/SC user
Group:		Text tools
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz
Source1:	http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz.asc
Requires:	perl-pcsc-perl >= 1.4.2 ccid
Buildrequires:	pcsc-lite-devel
URL:		http://ludovic.rousseau.free.fr/softwares/pcsc-tools/

%description
This package contains some tools useful for a PC/SC user.
- pcsc_scan (Ludovic Rousseau <ludovic.rousseau@free.fr>)
    regularly scans every PC/SC reader connected to the host
    if a card is inserted or removed a "line" is printed
- ATR_analysis (Christophe Levantis and Ludovic Rousseau)
    Perl script used to parse the smart card ATR.
    This script is called (by default) by pcsc_scan
- smartcard_list.txt (Ludovic Rousseau)
    This list contains ATR of some cards. The list is used by
    ATR_analysis to find a card model corresponding to the ATR.
- scriptor (Lionel Victor <lionel.victor@unforgettable.com>)
    A Perl script to send commands to a smart card. You can use a file
    containing the commands or stdin.
- gscriptor (Lionel Victor <lionel.victor@unforgettable.com>)
    A Perl script to send commands to a smart card with GTK-based
    graphical interface.

%prep
%setup -q
bzip2 -9 Changelog

%build
%make

%install
%make DESTDIR=%{buildroot}/usr install

%files
%doc README TODO Changelog.bz2
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/pcsc/smartcard_list.txt



%changelog
* Sun Jun 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.20-1mdv2012.0
+ Revision: 806024
- version update 1.4.20

* Tue Aug 31 2010 Tomas Kindl <supp@mandriva.org> 1.4.17-1mdv2011.0
+ Revision: 574740
- update to 1.4.17
- drop p0 as it's already included upstream...

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 1.4.15-4mdv2011.0
+ Revision: 574308
- rebuild for new pcsclite

* Tue Sep 15 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.4.15-3mdv2010.0
+ Revision: 442937
- add ccid to requires

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Feb 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.15-1mdv2009.1
+ Revision: 340648
- update to new version 1.4.15

* Sun May 11 2008 Frederik Himpe <fhimpe@mandriva.org> 1.4.14-1mdv2009.0
+ Revision: 205891
- New version

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.4.10-1mdv2008.1
+ Revision: 136654
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.10-1mdv2008.0
+ Revision: 80713
- don't package LICENCE
- use Fedora license policy
- new release 1.4.10

* Sat Jul 14 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.9-1mdv2008.0
+ Revision: 52109
- buildrequires pcsc-lite-devel not pcsclite-devel
- requires perl-pcsc-perl >= 1.4.2, not = 1.4.2 (fixes install, thanks Frederik Himpe)
- new release 1.4.9

* Mon May 28 2007 Andreas Hasenack <andreas@mandriva.com> 1.4.8-1mdv2008.0
+ Revision: 32039
- updated to version 1.4.8
- removed old changelog from spec file

