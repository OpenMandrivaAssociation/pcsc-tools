%define debug_package %{nil}

Summary:	PCSC tools useful for a PC/SC user
Name:		pcsc-tools
Version:	1.4.21
Release:	3
License:	GPLv2+
Group:		Text tools
Url:		http://ludovic.rousseau.free.fr/softwares/pcsc-tools/
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz
Source1:	http://ludovic.rousseau.free.fr/softwares/pcsc-tools/%{name}-%{version}.tar.gz.asc
Buildrequires:	pkgconfig(libpcsclite)
Requires:	ccid
Requires:	perl-pcsc-perl >= 1.4.2

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

