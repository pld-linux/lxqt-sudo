#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	GUI frontend for sudo/su
Summary(pl.UTF-8):	Interfejs graficzny dla sudo/su
Name:		lxqt-sudo
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-sudo/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3e6001b5f4556abc57281e44a7663a45
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI frontend for sudo/su.

%description -l pl.UTF-8
Interfejs graficzny dla sudo/su.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxdoas
%attr(755,root,root) %{_bindir}/lxqt-sudo
%attr(755,root,root) %{_bindir}/lxsu
%attr(755,root,root) %{_bindir}/lxsudo
%dir %{_datadir}/lxqt/translations/%{name}
%{_mandir}/man1/lxqt-sudo.1*
%{_mandir}/man1/lxsu.1*
%{_mandir}/man1/lxsudo.1*
%{_mandir}/man1/lxdoas.1
