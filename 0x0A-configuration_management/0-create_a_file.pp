#creating a file with puppet
$file_path = '/tmp/school'

file {'creating a file':
ensure => file,
mode => '0744',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet',
path => $file_path
}
