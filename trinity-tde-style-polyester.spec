%bcond clang 1

# TDE variables
%define tde_pkg tde-style-polyester
%define tde_prefix /opt/trinity


%define _disable_ld_no_undefined 1

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Domino widget style and twin decoration for TDE
Group:		Graphical desktop/TDE
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/themes/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:  trinity-tdelibs-devel >= %{version}
BuildRequires:  trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# JPEG support
BuildRequires:  pkgconfig(libjpeg)

BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  librsvg

%description
Domino is a style with a soft look. It allows to fine adjust the shininess
of the widgets by customizable color gradients.


%files
%defattr(-,root,root)
%{tde_prefix}/%{_lib}/trinity/plugins/styles/polyester.la
%{tde_prefix}/%{_lib}/trinity/plugins/styles/polyester.so
%{tde_prefix}/%{_lib}/trinity/tdestyle_polyester_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_polyester_config.so
%{tde_prefix}/%{_lib}/trinity/twin3_polyester.la
%{tde_prefix}/%{_lib}/trinity/twin3_polyester.so
%{tde_prefix}/%{_lib}/trinity/twin_polyester_config.la
%{tde_prefix}/%{_lib}/trinity/twin_polyester_config.so
%{tde_prefix}/share/apps/tdedisplay/color-schemes/PolyesterBlue.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/PolyesterEmerald.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/PolyesterOrangeJuice.kcsrc
%{tde_prefix}/share/apps/tdestyle/themes/polyester.themerc
%{tde_prefix}/share/apps/twin/polyester.desktop

