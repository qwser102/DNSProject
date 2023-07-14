import os
import codecs
file_path='/etc/named.rfc1912.zones'

#search for single domain
def domain_search():
    f = codecs.open( file_path, 'r', 'utf-8', buffering=True )
    key1 = 'zheng'
    key2 = 'file'
    list_domain = []
    for l in f.readlines():
        if key1 in l and key2 in l:
            n = l
            n = n.replace( 'file', '' )
            n = n.replace( '"', '' )
            n = n.replace( 'data/', '' )
            n = n.replace( ' ', '' )
            n = n.replace('.zheng','')
            list_domain.append( n )
    f.close()
    return list_domain

#search for extensive domain
def extensive_domain_search():
    f = codecs.open( file_path, 'r', 'utf-8', buffering=True )
    key1 = 'extensive'
    key2 = 'file'
    list_extensive = []
    for l in f.readlines():
        if key1 in l and key2 in l:
            n = l
            n = n.replace( 'file', '' )
            n = n.replace( '"', '' )
            n = n.replace( 'data/', '' )
            n = n.replace(' ','')
            n = n.replace( '.extensive', '' )
            list_extensive.append( n )
    f.close()
    return list_extensive

#add single domain
def add_domain(ip,domain_name):
    status = os.popen( '/usr/bin/bash ./script/add_domain.sh {} {}'.format(ip,domain_name) ).readlines()
    print( 'status=' + str( status ) )
    return status

#add extensive domain
def add_extensive_domain(ip,extensive_domain_name):
    status = os.popen('/usr/bin/bash ./script/add_extensive_domain.sh {} {}'.format(ip,extensive_domain_name)).readlines()
    #status = 'success!!\n'
    print('status=' + str(status))
    return status

#delete single domain
def domain_delete(domain_name):
    status = os.popen('/usr/bin/bash ./script/delete_domain.sh {}'.format(domain_name)).readlines()
    #status='success!!\n'
    print('status='+str(status))
    return status

#delete extensive domain
def extensive_domain_delete(domain_name):
    status = os.popen('/usr/bin/bash ./script/delete_extensive_domain.sh {}'.format(domain_name)).readlines()
    print('status='+str(status))
    return status

#dns status monitor
def dns_status():
    status = os.popen( 'systemctl status named |grep Active' ).readlines()
    print(status)
    return status


#test
#add_extensive_domain('127.0.0.1','www.test.com')