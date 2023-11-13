# Changing the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec {'hard_limit':
  provider => shell,
  command  => 'sudo sed -i "s/5/10000/" /etc/security/limits.conf',
}

exec {'soft_limit':
  provider => shell,
  command  => 'sudo sed -i "s/4/10000/" /etc/security/limits.conf',
}
