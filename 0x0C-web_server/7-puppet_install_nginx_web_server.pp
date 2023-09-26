# Installs Nginx web server (w/ Puppet)

exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo bash -c "echo Hello World!" > /var/www/html/index.nginx-debian.html ; sudo sed -i "s#server_name _;#server_name _;\n\trewrite ^\/redirect_me https://github.com/A-fethi permanent;#" /etc/nginx/sites-available/default ; sudo service nginx restart',
  provider => shell,
}
