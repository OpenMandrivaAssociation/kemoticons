%define major 5
%define libname %mklibname KF5Emoticons %{major}
%define devname %mklibname KF5Emoticons -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kemoticons
Version:	5.116.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 Emoticons framework
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Service)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 Emoticons framework.

%package -n %{libname}
Summary: The KDE Frameworks 5 Emoticons library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 Emoticons library.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Emoticons library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Emoticons library.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/kemoticons.*categories
%{_datadir}/emoticons
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%dir %{_libdir}/qt5/plugins/kf5/emoticonsthemes
# FIXME may want to package individual themes separately if they
# become too big
%{_libdir}/qt5/plugins/kf5/emoticonsthemes/*
%{_libdir}/qt5/plugins/kf5/*.so

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
