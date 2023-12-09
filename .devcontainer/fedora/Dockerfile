FROM fedora:39

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

# Install dependencies
RUN sudo dnf update -y && sudo dnf upgrade -y && sudo dnf install -y \
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
