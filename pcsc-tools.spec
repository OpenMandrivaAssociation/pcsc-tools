%define name pcsc-tools
%define version 1.4.7

%define num_release 1
%define release %mkrel %num_release

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Summary:	PCSC tools useful for a PC/SC user
Group:		Text tools
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz
Source1:	http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz.asc
Requires:	perl-pcsc-perl = 1.4.2
Buildrequires: libpcsclite-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
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
rm -rf %{buildroot}
%make DESTDIR=%{buildroot}/usr install

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc LICENCE README TODO Changelog.bz2
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/pcsc/smartcard_list.txt


%{!?_with_unstable:* %(LC_ALL=C date +"%a %b %d %Y") %{packager} %{version}-%{release}}
%{!?_with_unstable: - rebuild of %{version}-%{rel}%{distsuffix} for %{distversion}}
* Mon Mar 27 2006 Andreas Hasenack <andreas@mandriva.com> 1.4.4-2%{distsuffix}
- small spec cleanups
- don't use file lists

* Mon Mar 27 2006 Olivier Lahaye <olivier.lahaye1@free.fr> 1.4.4-1%{distsuffix}
- New version 1.4.4.

* Wed Mar 22 2006 Olivier Lahaye <olivier.lahaye1@free.fr> 1.4.2-2%{distsuffix}
- Updated Requires (from pcsc-perl to perl-pcsc-perl).

* Wed Mar 08 2006 Olivier Lahaye <olivier.lahaye1@free.fr> 1.4.2-1%{distsuffix}
- Initial packaging.
