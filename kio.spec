%define major 5
%define libname %mklibname KF5KIO %{major}
%define devname %mklibname KF5KIO -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kio
Version: 5.31.0
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
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(mit-krb5-gssapi)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Bookmarks)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5DocTools)
BuildRequires: acl-devel
BuildRequires: attr-devel
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

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}
%find_lang kcm_webshortcuts || touch kcm_webshortcuts.lang

%files -f %{name}%{major}.lang,kcm_webshortcuts.lang
%{_sysconfdir}/xdg/accept-languages.codes
%{_sysconfdir}/xdg/kshorturifilterrc
%{_bindir}/*
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
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
%lang(sv) %{_mandir}/sv/man8/*
%lang(uk) %{_mandir}/uk/man8/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*
%{_libdir}/cmake/KF5KIO
