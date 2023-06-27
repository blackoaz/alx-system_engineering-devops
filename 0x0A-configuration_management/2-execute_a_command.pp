#puppet file for killing a process using exec
exec {'killmenow':
    command => 'pkill killmenow',
    path    => ['/usr/bin', '/usr/sbin',]
}
