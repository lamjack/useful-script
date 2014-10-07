#!/bin/bash

### 检查是否具有root权限
if [[ "$(id -u)" != '0' ]]; then
	echo "You have no permission to run $0 as non-root user. Use sudo Please!"
	exit 1
fi

clear

### 虚拟主机路径配置
email='linjue@wilead.com'
wwwroot='/Users/jack/WebServer/www'

### 设置虚拟主机信息
domain="www.wilead.com"
echo "Please input domain:"
read -p "(Default domain: www.wilead.com):" domain
if [[ "$domain" == "" ]]; then
	domain="www.wilead.com"
fi
if [[ ! -f "/opt/local/apache2/conf/extra/vhost/$domain-vhost.conf" ]]; then
	echo "========================="
	echo "domain=$domain"
	echo "========================="
else
	echo "========================="
	echo "$domain is exist!"
	echo "========================="
	exit 1
fi

echo "Do you want to add more domain name? (y/n)"
read add_more_domain

if [[ "$add_more_domain" == 'y' ]]; then
	echo "Type domainname,example(bbs.wilead.com blog.wilead.com):"
	read moredomain
	echo "========================="
	echo domain list="$moredomain"
	echo "========================="
	moredomainname="$moredomain"
fi

echo "Input virtual host wwwroot:($wwwroot/$domain):"
read input_webroot

if [[ "$input_webroot" != '' ]]; then
	vhostdir="$input_webroot"
else
	vhostdir="$wwwroot/$domain"
fi

### 虚拟主机配置目录不存在，则创建目录
if [[ ! -d /opt/local/apache2/conf/extra/vhost ]]; then
	mkdir /opt/local/apache2/conf/extra/vhost
fi

echo "Create virtual host directory..."

if [[ ! -d "$wwwroot/$domain" ]]; then
	mkdir -p $vhostdir
fi

echo "set permission of virtual host directory..."
chown -R Jack:staff $vhostdir

cat >/opt/local/apache2/conf/extra/vhost/$domain-vhost.conf<<eof

<VirtualHost *:80>
    ServerAdmin $email
    DocumentRoot "$vhostdir"
    ServerName $domain
    ServerAlias $moredomainname
    ErrorLog "/Users/jack/WebServer/logs/$domain-error_log"
    CustomLog "/Users/jack/WebServer/logs/$domain-access_log" common
</VirtualHost>
eof

echo "Test Apache2 configure file..."
/opt/local/apache2/bin/apachectl -t
echo ''
echo "Restarting Apache2..."
/opt/local/apache2/bin/apachectl restart
echo "Create virtual host success!"