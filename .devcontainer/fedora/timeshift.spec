# This spec file is sourced from https://src.fedoraproject.org/rpms/timeshift/blob/f39/f/timeshift.spec
# and adapted to the newer version of timeshift with the Meson build system.
# This is only meant to quickly create a RPM packages for testing and debugging.


# This package needs to be run as root and may
# run for a long time, thus we build with full
# hardening. This flags is enabled by default
# on recent Fedora releases, but we need to
# specify it for EPEL <= 7 explicitly.
%global _hardened_build 1

Name:           timeshift
Summary:        System restore tool for Linux
Version:        1.0.0
Release:        %autorelease

License:        GPLv3+ or LGPLv3+
Source0:        timeshift.tar.gz

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  vala

Requires:       cronie
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       psmisc
Requires:       rsync

# For btrfs systems
Recommends:     btrfs-progs

%description
Timeshift for Linux is an application that provides functionality similar to
the System Restore feature in Windows and the Time Machine tool in Mac OS.
Timeshift protects your system by taking incremental snapshots of the file
system at regular intervals. These snapshots can be restored at a later date
to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files
are shared between snapshots which saves disk space. Each snapshot is a full
system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS
filesystem. BTRFS snapshots are supported only on BTRFS systems having an
Ubuntu-type subvolume layout (with @ and @home subvolumes).

%prep
%autosetup -n %{name} -p1

%build
meson setup --buildtype=release build_rpm && meson compile -C build_rpm

%install
pushd build_rpm
  sudo meson install --destdir %{buildroot}
popd

%find_lang %{name}

# Redefine install dirs (not allowed for fedora repos!)
%define _datadir /usr/local/share
%define _bindir /usr/local/bin
%define _mandir /usr/local/share/man
%define _sysconfdir /usr/local/etc

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md
%{_bindir}/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-gtk.1*
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/%{name}-boot
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/%{name}-hourly
%ghost %attr(664, root, root) %{_sysconfdir}/%{name}.json
%config %{_sysconfdir}/%{name}/default.json

%changelog
%autochangelog