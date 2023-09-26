#!/usr/bin/env bsah
# Installs Nginx web server (w/ Puppet)

exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo bash -c echo "Hello World!" > /var/www/html/index.nginx-debian.html',
  provider => shell,
}
