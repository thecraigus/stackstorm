import requests
import json
from netmiko import ConnectHandler
import sys
import re 

syslogmessage =  sys.argv[2]

interface = re.search('on(.+)from',syslogmessage).group(1)
print (interface)
device = sys.argv[1]

dev = {
    'device_type': 'cisco_ios',
    'host':device,
    'username': 'admin',
    'password': 'password123'
}

net_connect = ConnectHandler(**dev)

interface_output = net_connect.send_command('show interface {}'.format(interface))





bot_token = 'ZDZmYzU2MGUtM2ZhNS00Y2UyLWIzN2EtYWE0YjMzMzhkY2QzMTU3M2I3ZDgtMTMw_9d8f-c4e20787cdbf'
roomm_id = 'Y2lzY29zcGFyazovL3VzL1JjLThmNjgtN2RiZTgwOTZjNDUz'
message = 'OSPF Peering Failure Detected On Device {} \n {}' .format(sys.argv[1],sys.argv[2])
api_url = 'https://webexapis.com/'

headers = {'Authorization': 'Bearer {}'.format(
    bot_token), 'content-type': 'application/json'}
payload = {
    "roomId": roomm_id,
    "markdown": message+'\n'+interface_output
}



post_message = requests.post(
    url=api_url+'/v1/messages', headers=headers, data=json.dumps(payload))

print (post_message.content)
