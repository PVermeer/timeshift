#!/bin/bash

# Script for vscode tasks

set -e

project_dir=$PWD

# Prepare rpm build
rm -rf ~/rpmbuild
rpmdev-setuptree
cp ./.devcontainer/fedora/timeshift.spec ~/rpmbuild/SPECS/

# Prepare source
rm -rf /tmp/timeshift
mkdir -p /tmp/timeshift
cp -r ./ /tmp/timeshift/
cd /tmp/
tar -cvzf timeshift.tar.gz timeshift
mv /tmp/timeshift.tar.gz ~/rpmbuild/SOURCES/
cd $project_dir

# Build from source
rpmbuild -bb ~/rpmbuild/SPECS/timeshift.spec

# Copy RPM's to repo
rm -rf ./build_rpm
mkdir -p ./build_rpm
cp -r ~/rpmbuild/RPMS/* ./build_rpm/
