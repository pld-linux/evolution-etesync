Summary:	Module for accessing EteSync accounts through Evolution
Summary(pl.UTF-8):	Moduł pozwalający na dostęp do kont EteSync z poziomu Evolution
Name:		evolution-etesync
Version:	1.1.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	https://download.gnome.org/sources/evolution-etesync/1.1/%{name}-%{version}.tar.xz
# Source0-md5:	151e3b662ae61715019c4f84daedfd08
URL:		https://wiki.gnome.org/Apps/Evolution
BuildRequires:	cmake >= 3.1
BuildRequires:	evolution-data-server-devel >= 3.34.0
BuildRequires:	evolution-devel >= 3.34.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	intltool
BuildRequires:	libetebase-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= 3.34.0
Requires:	evolution-data-server >= 3.34.0
Requires:	glib2 >= 1:2.46
Requires:	gtk+3 >= 3.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module for accessing EteSync accounts through Evolution.

%description -l pl.UTF-8
Moduł pozwalający na dostęp do kont EteSync z poziomu Evolution.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/evolution/modules/module-etesync-configuration.so
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendetesync.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendetesync.so
%attr(755,root,root) %{_libdir}/evolution-data-server/credential-modules/module-etesync-credentials.so
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-etesync-backend.so
%dir %{_libdir}/evolution-etesync
%attr(755,root,root) %{_libdir}/evolution-etesync/libevolution-etesync.so
%{_datadir}/metainfo/org.gnome.Evolution-etesync.metainfo.xml
