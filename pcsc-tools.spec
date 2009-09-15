%define name pcsc-tools
%define version 1.4.15

%define num_release 1
%define release %mkrel 3

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
%doc README TODO Changelog.bz2
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/pcsc/smartcard_list.txt

