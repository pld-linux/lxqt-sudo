#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-sudo
Name:		lxqt-sudo
Version:	0.10.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	7671aebf30a28cb27438dd87de0a589e
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.10.0
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	xdg-utils >= 1.1.0
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-sudo

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-sudo
%attr(755,root,root) %{_bindir}/lxsu
%attr(755,root,root) %{_bindir}/lxsudo
%dir %{_datadir}/lxqt/translations/%{name}
%{_mandir}/man1/lxqt-sudo.1*
%{_mandir}/man1/lxsu.1*
%{_mandir}/man1/lxsudo.1*
