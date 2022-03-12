#  Create a custom HTTP header response

 include stdlib


class nginxcustom { 
   file { '/etc/puppetlabs/nginx/headers.conf': 
     ensure => file, 
     group => 'root',
     owner => 'root', 
     mode => '0644', 
     source =>'puppet:///modules/nginxcustom/headers.conf', 
    }
}


#Nginx directive to add include statement 
pe_nginx::directive { 'include custom headers': 
directive_ensure => 'present', 
target => '/etc/puppetlabs/nginx/conf.d/proxy.conf', 
directive_name => 'include', 
value => 'headers.conf', 
server_context => $::fqdn, } 
}


add_header X-Frame-Options SAMEORIGIN always;

