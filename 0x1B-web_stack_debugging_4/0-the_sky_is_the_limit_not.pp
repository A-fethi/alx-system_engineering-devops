# Fixing Length Failed Requests

exec {'Hot Fix':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
}
