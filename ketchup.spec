Summary:	Update utility for Linux kernel sources
Summary(pl):	Narz�dzie do uaktualniania �r�de� j�dra Linuksa
Name:		ketchup
Version:	0.9.8
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.selenic.com/ketchup/%{name}-%{version}.tar.bz2
# Source0-md5:	6fbe53beac455245e1e8ae92acdccbcc
Patch0:		%{name}-ck.patch
URL:		http://www.selenic.com/ketchup/wiki/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility can update (or install) Linux kernel sources
automatically. It can search for the newest kernel in numerous trees
(vanilla, rc, tiny, mm, mjb, etc.).

It can also automatically download the needed patches (and apply them)
to create the newest repository from an old one.

%description -l pl
To narz�dzie potrafi automatycznie uaktualnia� (lub instalowa�) �r�d�a
j�dra Linuksa. Mo�e szuka� najnowszego j�dra w r�nych drzewach
(vanilla, rc, tiny, mm, mjb itp.).

Potrafi tak�e automatycznie �ci�ga� potrzebne �aty (i nak�ada� je),
aby stworzy� najnowsze repozytorium ze starszego.

%prep
%setup -qc
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

install ketchup $RPM_BUILD_ROOT%{_bindir}
cp -a ketchup.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc contrib
%attr(755,root,root) %{_bindir}/ketchup
%{_mandir}/man1/ketchup.1*
