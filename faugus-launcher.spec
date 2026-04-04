Name:           faugus-launcher
Version:        1.17.5
Release:        1
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
Group:          Games
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Source0:        https://github.com/Faugus/faugus-launcher/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:    meson

BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  python-devel

Requires:	python
Requires:	python-gobject
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(icoextract)
Requires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(filelock)
Requires:	python%{pyver}dist(vdf)
Requires:	python%{pyver}dist(psutil)
Requires:	umu-launcher
Requires:	imagemagick
Requires:	typelib(AyatanaAppIndicator3)
Requires:	canberra-gtk3

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

%files -f faugus-launcher.lang
%license LICENSE
%doc README.md
%{_bindir}/faugus-launcher
%{_bindir}/faugus-run
%{python3_sitelib}/faugus/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/icons/hicolor/256x256/apps/faugus-mono.svg
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/faugus-launcher/*
%{_datadir}/metainfo/faugus-launcher.metainfo.xml
