FROM fedora:39

# Install dependencies
RUN dnf update -y && dnf upgrade -y && dnf install -y \
  which \
  git \
  meson \
  desktop-file-utils \
  gettext \
  libappstream-glib \
  'pkgconfig(json-glib-1.0)' \
  'pkgconfig(libsoup-2.4)' \
  'pkgconfig(glib-2.0)' \
  'pkgconfig(gio-unix-2.0)' \
  'pkgconfig(gtk+-3.0)' \
  'pkgconfig(gee-0.8)' \
  'pkgconfig(vte-2.91)' \
  xapps-devel \
  help2man \
  vala \
  cronie \
  hicolor-icon-theme \
  polkit \
  psmisc \
  rsync \
  btrfs-progs \
  vala-language-server \
  gdb \
  nautilus \
  rpmdevtools \
  rpmlint
