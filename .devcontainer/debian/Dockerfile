FROM mcr.microsoft.com/devcontainers/base:bullseye

# Vala language server repository
RUN \
  echo 'deb http://download.opensuse.org/repositories/home:/Prince781/Debian_11/ /' | sudo tee /etc/apt/sources.list.d/home:Prince781.list \
  &&\
  curl -fsSL https://download.opensuse.org/repositories/home:Prince781/Debian_11/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_Prince781.gpg > /dev/null

# Install dependencies
RUN apt update -y && apt upgrade -y && apt install -y \
  meson \
  help2man \
  gettext \
  valac \
  libvte-2.91-dev \
  libgee-0.8-dev \
  libjson-glib-dev \
  libxapp-dev \
  cron \
  btrfs-progs \
  vala-language-server \
  gdb \
  nautilus
