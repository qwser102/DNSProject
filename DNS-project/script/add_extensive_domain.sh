#!/bin/bash
ip=$1
name=$2

set -e
function check_ip() {
IP=$1
if [[ $IP=~^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]];then
	filed1=$(echo $IP|cut -d. -f1)
	filed2=$(echo $IP|cut -d. -f2)
	filed3=$(echo $IP|cut -d. -f3)
	filed4=$(echo $IP|cut -d. -f4)
	if [ $filed1 -le 255 -a $filed2 -le 255 -a $filed3 -le 255 -a $filed4 -le 255 ];then
		echo "IP $IP is avaliable"
		return 0
	else
		echo "$IP is not avaliable !!"
		return 1
	fi
else
	echo "$IP is not avaliable !!"
	return 1
fi
}

check_ip $ip

function check_domain() {
domain=$1
if [ ! -f "/var/named/data${domain}.extensive" ];then
	echo "domain ${domain} is avaliable !"
	return 0
else
	echo "domain ${domain} has been used , please change another domain name !!!"
	return 1
fi
}

check_domain $name


cat >>/etc/named.rfc1912.zones<< EOF
zone "${name}" IN {
	type master;
        file "data/${name}.extensive";
};
EOF

cat >>/var/named/data/${name}.extensive<< EOF
\$TTL 1D
@	IN SOA	dns.${name}. root.${name}. (
					0	; serial
					1D	; refresh
					1H	; retry
					1W	; expire
					3H )	; minimum
	NS	dns.${name}.
dns.${name}	A	${ip}
*.${name}.	IN	${ip}
EOF

chown named:named /var/named/data/${name}.extensive
systemctl restart named
echo "add extensive domain ${name} success !"