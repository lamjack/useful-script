#!/bin/bash

### 检查是否具有root权限
if [[ "$(id -u)" != '0' ]]; then
	echo "You have no permission to run $0 as non-root user. Use sudo Please!"
	exit 1
fi

clear

wwwroot='/Users/Jack/WebServer/www'

echo "Please input domain that want to delete:"
read domain

if [[ "$domain" != '' ]]; then
	if [[ ! -f "/opt/local/apache2/conf/extra/vhost/$domain-vhost.conf" ]]; then
		echo "$domain is not exist"
	else
		rm -rf /opt/local/apache2/conf/extra/vhost/$domain-vhost.conf
	fi
else
	exit 1
fi

rm -rf "$wwwroot/$domain"
/opt/local/apache2/bin/apachectl restart

echo "$domain delete success"