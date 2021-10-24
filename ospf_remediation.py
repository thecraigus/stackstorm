from netmiko import ConnectHandler
import sys
import re 

syslogmessage =  sys.argv[2]

interface = re.search('on(.+)from',syslogmessage).group(1)

device = sys.argv[1]

dev = {
    'device_type': 'cisco_ios',
    'host':device,
    'username': 'admin',
    'password': 'password123'
}

net_connect = ConnectHandler(**dev)

remeditation_action = ['interface {}'.format(interface),'shutdown','no shut']

interface_output = net_connect.send_config_set(remeditation_action)
