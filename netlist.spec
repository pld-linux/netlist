Summary:	A program to list active Internet connections and sockets
Summary(pl.UTF-8):	Program pokazujący aktywne połączenia i gniazdka
Name:		netlist
Version:	2.1
Release:	1
License:	distributable
Group:		Networking
Source0:	http://www.openwall.com/linux/contrib/%{name}-%{version}.tar.gz
# Source0-md5:	1e987e62c82a19418548681f5cfa2e90
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

%description -l pl.UTF-8
Uruchomiony przez nieuprzywilejowanego użytkownika, netlist pokazuje
aktywne połączenia oraz nasłuchujące gniazdka tego użytkownika.

Uruchomione przez roota lub użytkownika należącego do grupy z dostępem
do /proc, pokazuje wszystkie aktywne gniazdka TCP, UDP i raw w
systemie.

netlist został stworzony by opanować restryktywne tendencje w
bezpieczeństwie. Użycie netlist musi być zgodne z tymi intencjami. W
pliku LICENSE znajdują się stosowne informacje.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(2755,root,proc) %{_bindir}/netlist
%{_mandir}/man1/netlist.1*
