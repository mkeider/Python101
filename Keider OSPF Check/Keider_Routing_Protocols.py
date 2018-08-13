import re
import csv
import json


#This script simply checks if the Routing Protocols: BGP, EIGRP, or OSPF are in use


#Configuration Snippet used for Testing
routing_protocol = '''

hostname Router
router ospf 1600
 router-id 1.1.1.1
 log-adjacency-changes detail
 auto-cost reference-bandwidth 100000
 passive-interface Vlan300
 network 10.1.1.1 0.0.0.0 area 0
 network 10.2.2.1 0.0.0.0 area 0
default-information originate

router eigrp 100

router bgp 300
'''

#Cisco Hostname REGEX Patterns
Hostname = re.findall(r"^(hostname)\s(.\S+)", routing_protocol, re.MULTILINE)
for match in Hostname:
    print(match[1])


#Protocol Checks in Protocol List against REGEX Patterns
#Protocol List
protocol =['eigrp', 'ospf', 'bgp']

for test in protocol:
    if re.findall(r"^(router) (ospf)\s(\d+)", routing_protocol, re.MULTILINE):
        print('Running OSPF')
        break
for test in protocol:
    if re.findall(r"^(router) (eigrp)\s(\d+)", routing_protocol, re.MULTILINE):
        print('Running EIGRP')
        break

for test in protocol:
    if re.findall(r"^(router) (bgp)\s(\d+)", routing_protocol, re.MULTILINE):
        print('Running BGP')
        break