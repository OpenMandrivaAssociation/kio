%define major 5
%define libname %mklibname KF5KIO %{major}
%define devname %mklibname KF5KIO -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio
Version: 5.116.0
Release: 3
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Patch0: https://invent.kde.org/frameworks/kio/-/commit/341a75c7e42ea8bcea07d0a0c0044a5a4f342e07.patch
Summary: The KDE Frameworks 5 framework for handling Input and Output (I/O)
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(mit-krb5-gssapi)
BuildRequires: cmake(Qt5UiPlugin)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Bookmarks)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KDED)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(com_err)
BuildRequires: pkgconfig(mount)
BuildRequires: acl-devel
BuildRequires: attr-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: openmandriva-kde-translation
Requires: %{libname} = %{EVRD}
Requires: kded
Conflicts: kdelibs4support < 5.30.0
Obsoletes: kcookiejar < 5.240.0-1
# Used to be shared with plasma6, changed names now
Obsoletes: kio-dbus-services < 5.240.0-1
Recommends: switcheroo-control

%description
The KDE Frameworks 5 framework for handling Input and Output (I/O).

%package -n %{libname}
Summary: The KDE Frameworks 5 framework for handling Input and Output (I/O)
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 framework for handling Input and Output (I/O).

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: pkgconfig(Qt5Concurrent)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%files designer
%{_libdir}/qt5/plugins/designer/*.so

# This is split out because if clashes with plasma6-kio-extras
%package kcm_trash
Summary: KCM 5.x module controlling the trash
Group: System/Libraries
Requires: kio = %{EVRD}
Supplements: plasma-desktop < 5.27.50

%description kcm_trash
KCM 5.x module controlling the trash

%files kcm_trash
%{_datadir}/applications/kcm_trash5.desktop

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major} --with-man --with-html --all-name

cd %{buildroot}%{_libdir}/qt5/plugins/kf5/kio
for i in kio_*.so; do
	mv $i ${i/kio_/}
done

# Don't clash with P6
mv %{buildroot}%{_datadir}/applications/kcm_trash.desktop %{buildroot}%{_datadir}/applications/kcm_trash5.desktop

%files -f %{name}%{major}.lang
%{_datadir}/qlogging-categories5/kio.*categories
%{_sysconfdir}/xdg/accept-languages.codes
%{_sysconfdir}/xdg/kshorturifilterrc
%{_bindir}/*
%{_datadir}/kconf_update/filepicker.upd
%{_datadir}/kservicetypes5/*
%{_datadir}/kservices5/*
%{_datadir}/knotifications5/*
%{_datadir}/kf5/kcookiejar
%{_datadir}/applications/ktelnetservice5.desktop
%{_datadir}/dbus-1/services/org.kde.kcookiejar5.service
%{_datadir}/dbus-1/interfaces/*
%{_libdir}/qt5/plugins/kcm*.so
%{_libdir}/qt5/plugins/kf5/kded
%{_libdir}/qt5/plugins/kf5/kio
%{_libdir}/qt5/plugins/kf5/kiod
%{_libdir}/qt5/plugins/kf5/urifilters
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets
%{_libdir}/libexec/kf5/*
%{_mandir}/man8/*
%{_datadir}/dbus-1/services/org.kde.kiod5.service
%{_datadir}/dbus-1/services/org.kde.kioexecd.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver.service
%{_datadir}/dbus-1/services/org.kde.kssld5.service

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*
%{_libdir}/cmake/KF5KIO
%{_datadir}/kdevappwizard/templates/kioworker.tar.bz2

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
