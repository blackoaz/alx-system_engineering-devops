#create a file with a puppet
$file_path = '/tmp/school'
file { 'create_file':
    ensure  => 'file',
    content => 'I love Puppet',
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data',
    path    => $file_path
}
