# change the nginx file limit
exec { 'Change nginx limit':
  command => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudoservice nginx restart',
  provider => shell,
}
