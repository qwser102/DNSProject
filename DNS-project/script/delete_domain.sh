domain_name=$1
file="/etc/named.rfc1912.zones"
data_file="/var/named/data/${domain_name}.zheng"
function domain_name_check()
{
domain_name=$1
cat -n $file |grep "${domain_name}".zheng -B 2 -A 1
if [ $? -ne 1 ];then
	echo 'domain exist , can been deleted'
else 
	echo 'domain does not exist ,nothing to do !!!'
	exit 1
fi
}

domain_name_check $domain_name 

set -e
first_num=`cat -n $file |grep "${domain_name}".zheng -B 2 -A 1 |awk '{print $1}'|head -n 1`
last_num=$[$first_num+3]
#echo $last_num
sed -i "${first_num},${last_num}d" ${file}

rm -rf $data_file

systemctl restart named
echo "delete ${domain_name} success !"

