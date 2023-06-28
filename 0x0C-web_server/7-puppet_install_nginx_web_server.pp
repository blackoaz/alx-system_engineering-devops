# Define the class for Nginx installation and configuration
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => '
      server {
        listen 80;
        server_name _;
        
        location / {
          return 200 "Hello World!";
        }
        
        location /redirect_me {
          return 301 https://stackoverflow.com/;
        }
      }
    ',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Apply the Nginx class to the node
include nginx
