Summary:	A program to list active Internet connections and sockets
Summary(pl):	Program pokazuj±cy aktywne po³±czenia i gniazdka
Name:		netlist
Version:	2.0
Release:	2
License:	distributable
Group:		Networking
Source0:	http://www.openwall.com/linux/contrib/%{name}-%{version}.tar.gz
# Source0-md5:	2008aeacf13d8eee524909b9e143d62b
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
Uruchomiony przez nieuprzywilejowanego u¿ytkownika, netlist pokazuje
aktywne po³±czenia oraz nas³uchuj±ce gniazdka tego u¿ytkownika.

Uruchomione przez roota lub u¿ytkownika nale¿±cego do grupy z dostêpem
do /proc, pokazuje wszystkie aktywne gniazdka TCP, UDP i raw w
systemie.

netlist zosta³ stworzony by opanowaæ restryktywne tendencje w
bezpieczeñstwie. U¿ycie netlist musi byæ zgodne z tymi intencjami. W
pliku LICENSE znajduj± siê stosowne informacje.

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
