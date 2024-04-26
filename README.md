# DNSProject
本服务需要部署到安装了DNS服务的服务器上

DNS服务部署

centos

sudo yum install -y bind bind-utils

#vim /etc/named.conf
options {
	listen-on port 53 { 127.0.0.1;192.168.2.129; };    #添加本地地址
	listen-on-v6 port 53 { ::1; };
	directory 	"/var/named";
	dump-file 	"/var/named/data/cache_dump.db";
	statistics-file "/var/named/data/named_stats.txt";
	memstatistics-file "/var/named/data/named_mem_stats.txt";
	recursing-file  "/var/named/data/named.recursing";
	secroots-file   "/var/named/data/named.secroots";
	allow-query     { any; };       # 修改允许所有节点访问

   ...
   }

systemctl start named 

systemctl enable named 
