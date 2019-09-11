%define major 5
%define libname %mklibname KF5KIO %{major}
%define devname %mklibname KF5KIO -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio
Version: 5.62.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 framework for handling Input and Output (I/O)
URL: http://kde.org/
License: GPL
Group: System/Libraries
Patch0: kio-5.24.0-fileplaces.patch
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(mit-krb5-gssapi)
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
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(com_err)
BuildRequires: acl-devel
BuildRequires: attr-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: openmandriva-kde-translation
Requires: %{libname} = %{EVRD}
Conflicts: kdelibs4support < 5.30.0

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

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/qlogging-categories5/kio.categories
%{_sysconfdir}/xdg/accept-languages.codes
%{_sysconfdir}/xdg/kshorturifilterrc
%{_bindir}/*
%{_datadir}/kconf_update/filepicker.upd
%{_datadir}/kservicetypes5/*
%{_datadir}/kservices5/*
%{_datadir}/knotifications5/*
%{_datadir}/kf5/kcookiejar
%{_datadir}/dbus-1/*/*
%{_datadir}/applications/*
%{_libdir}/qt5/plugins/kcm*.so
%{_libdir}/qt5/plugins/kf5/kded
%{_libdir}/qt5/plugins/kf5/kio
%{_libdir}/qt5/plugins/kf5/kiod
%{_libdir}/qt5/plugins/kf5/urifilters
%{_libdir}/libexec/kf5/*
%doc %{_docdir}/HTML/*/kioslave5
%doc %{_docdir}/HTML/*/kcontrol5
%{_mandir}/man8/*
%lang(ca) %{_mandir}/ca/man8/*
%lang(de) %{_mandir}/de/man8/*
%lang(es) %{_mandir}/es/man8/*
%lang(it) %{_mandir}/it/man8/*
%lang(nl) %{_mandir}/nl/man8/*
%lang(pt) %{_mandir}/pt/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
%lang(sv) %{_mandir}/sv/man8/*
%lang(uk) %{_mandir}/uk/man8/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*
%{_libdir}/cmake/KF5KIO

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
