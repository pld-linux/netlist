Summary:	A program to list active Internet connections and sockets
Summary(pl):	Program pokazuj�cy aktywne po��czenia i gniazdka
Name:		netlist
Version:	2.0
Release:	2
License:	distributable
Group:		Networking
Group(de):	Netzwerkwesen
Group(es):	Red
Group(pl):	Sieciowe
Group(pt_BR):	Rede
Source0:	http://www.openwall.com/linux/contrib/%{name}-%{version}.tar.gz
URL:		http://www.openwall.com/linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When run by a non-privileged user, netlist lists active Internet
connections and listening sockets of that user.

When run by root or a user with group access privileges for /proc,
netlist lists all active TCP, UDP, and raw sockets on the system.

netlist was created to oppose restrictive tendencies in security. Your
use of netlist must be in accordance with this intent. Please see the
LICENSE for information on this and other licensing conditions.

%description -l pl
Uruchomiony przez nieuprzywilejowanego u�ytkownika, netlist pokazuje
aktywne po��czenia oraz nas�uchuj�ce gniazdka tego u�ytkownika.

Uruchomione przez roota lub u�ytkownika nale��cego do grupy z dost�pem
do /proc, pokazuje wszystkie aktywne gniazdka TCP, UDP i raw w
systemie.

netlist zosta� stworzony by opanowa� restryktywne tendencje w
bezpiecze�stwie. U�ycie netlist musi by� zgodne z tymi intencjami. W
pliku LICENSE znajduj� si� stosowne informacje.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" CFLAGS="-c -Wall %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}

gzip -9nf LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,proc) %{_bindir}/netlist
%{_mandir}/man1/netlist.1*
