Summary:	A Chess Engine
Name:		phalanx
Version:	25
Release:	1
License:	GPLv2
Group:		Games/Boards
URL:		http://dusan.freeshell.org/phalanx/
Source0:	http://downloads.sourceforge.net/project/phalanx/Version%20XXIII%20Beta/phalanx-XXIII-beta.tgz
Source1:	sbook.phalanx.bz2
Source2:	learn.phalanx.bz2
Source3:	phalanx.sh.bz2
Patch0:		phalanx-23-rosa-format-security.patch
Provides:	chessengine

# TODO: either exclusivearch or regen opening books.
#       phalanx opening books are big/little endian sensitive

%description
Phalanx is a chess engine. It contains a text interface for playing
chess. Though it does not have any graphical interface, one can use
it inside some GUI chess interface such as Xboard or CSBoard,
serving as a chess engine.

%prep
%setup -q -n phalanx-XXIII

mv sbook.phalanx sbook.phalanx.bak
bzip2 -dc %{SOURCE1} > sbook.phalanx
bzip2 -dc %{SOURCE2} > learn.phalanx
bzip2 -dc %{SOURCE3} > phalanx.sh

%patch0 -p1

%build
%make	CFLAGS='%optflags -ffast-math' \
	DEFINES='-DGNUFUN -DPBOOK_DIR=\"%{_gamesdatadir}/%{name}\" -DSBOOK_DIR=\"%{_gamesdatadir}/%{name}\" -DECO_DIR=\"%{_gamesdatadir}/%{name}\"'

%install
install -D -m 755 phalanx %{buildroot}%{_gamesbindir}/phalanx.real
install -D -m 755 phalanx.sh %{buildroot}%{_gamesbindir}/phalanx

# install opening books
mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
install -m 644 eco.phalanx pbook.phalanx sbook.phalanx learn.phalanx %{buildroot}%{_gamesdatadir}/%{name}/

%files
%doc HISTORY README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}



%changelog
* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 22-6mdv2009.0
+ Revision: 258964
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 22-5mdv2009.0
+ Revision: 246856
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 22-3mdv2008.1
+ Revision: 124169
- kill re-definition of %%buildroot on Pixel's request
- import phalanx


* Tue Jul 19 2005 Abel Cheung <deaddog@mandriva.org> 22-3mdk
- Fix startup script

* Fri Jun 10 2005 Abel Cheung <deaddog@mandriva.org> 22-2mdk
- Rebuild
- Use large opening book

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 22-1mdk
- First Mandrake package
- P0: Build fix with newer gcc (source code is 4 yrs old)
- Use big secondary opening book and learning book from website
- ( Wish if I can put the 30MB huge opening book here :-> )
