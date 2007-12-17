%define	version	22
%define release	%mkrel 3

Summary:	A Chess Engine
Name:		phalanx
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://dusan.freeshell.org/phalanx/
Source0:	http://dusan.freeshell.org/phalanx/%{name}-%{version}.tar.bz2
Source1:	sbook.phalanx.bz2
Source2:	learn.phalanx.bz2
Source3:	phalanx.sh.bz2
Patch0:		phalanx-22.build.patch.bz2
Provides:	chessengine

# TODO: either exclusivearch or regen opening books.
#       phalanx opening books are big/little endian sensitive

%description
Phalanx is a chess engine. It contains a text interface for playing
chess. Though it does not have any graphical interface, one can use
it inside some GUI chess interface such as Xboard or CSBoard,
serving as a chess engine.

%prep
%setup -q -n Phalanx-XXII
%patch0 -p1 -b .newgcc

mv sbook.phalanx sbook.phalanx.bak
bzip2 -dc %{SOURCE1} > sbook.phalanx
bzip2 -dc %{SOURCE2} > learn.phalanx
bzip2 -dc %{SOURCE3} > phalanx.sh

%build
%make	CFLAGS='%optflags -ffast-math' \
	DEFINES='-DGNUFUN -DPBOOK_DIR=\"%{_gamesdatadir}/%{name}\" -DSBOOK_DIR=\"%{_gamesdatadir}/%{name}\" -DECO_DIR=\"%{_gamesdatadir}/%{name}\"'

%install
rm -rf %{buildroot}

install -D -m 755 phalanx %{buildroot}%{_gamesbindir}/phalanx.real
install -D -m 755 phalanx.sh %{buildroot}%{_gamesbindir}/phalanx

# install opening books
mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
install -m 644 eco.phalanx pbook.phalanx sbook.phalanx learn.phalanx %{buildroot}%{_gamesdatadir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}

