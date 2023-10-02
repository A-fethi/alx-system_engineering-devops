# Installing an Nginx server with custom HTTP header

exec { 'Update':
  provider => shell,
  command  => 'sudo apt-get update',
  before   => Exec['Nginx installation'],
}

exec { 'Nginx installation':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['Header'],
}

exec { 'Header':
  provider => shell,
  command  => 'sudo sed -i "s#server_name _;#server_name _;\n\tadd_header X-Served-By $(hostname);#" /etc/nginx/sites-available/default',
  before   => Exec['Restart'],
}

exec { 'Restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
