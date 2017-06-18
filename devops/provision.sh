#!/usr/bin/env bash

apt update
apt install -y python3-pip postgresql-9.5 postgresql-server-dev-9.5 ffmpeg
sudo -u postgres bash -c "createuser --createdb --echo --login --superuser vagrant "
sudo -u postgres bash -c "psql -c \"ALTER ROLE vagrant WITH PASSWORD 'vagrant';\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE vagrant;\""
cd /vagrant
sudo pip3 install --upgrade pip
sudo pip3 install -r requirements.txt