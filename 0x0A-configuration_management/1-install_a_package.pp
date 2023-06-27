#puppet file for installing flask
$package_name = 'flask'
package {$package_name:
    ensure   => '2.1.0',
    provider => 'pip3'
}
