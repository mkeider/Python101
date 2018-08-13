import re
import json
import csv

#Script is for LEGACY CISCO IOS

#This script runs OSPF configuration checks for the following parameters: 1.OSPF Enabled, 2. If Default-Information Originate is present,
#  3. If Auto-Cost Reference Bandwidth is in Best Practice, 4. If OSPF Router-ID is tied to Loopback Interface, 5. Lists all configured OSPF IP Subnets with Areas##

#OSPF Configuration Snippet used for Testing "OSPF Checks" script##
ospf = '''

interface Loopback0
 description Management IP address
 ip address 1.1.1.1 255.255.255.255
 
 interface Loopback2
 ip address 2.2.2.1 255.255.255.0

router ospf 1600
 router-id 1.1.1.1
 log-adjacency-changes detail
 auto-cost reference-bandwidth 10000
 passive-interface Vlan300
 network 10.1.1.1 0.0.0.0 area 0
 network 10.2.2.1 0.0.0.0 area 0
default-information originate

'''


#Result Dictionary for JSON output##
result = {
 "OSPF_ENABLED": [],
 "ROUTER_ID": {},
 "DEFAULT_ORIGINATE": {},
 "REFERENCE_BANDWIDTH": {},
 "OSPF_NETWORKS": []
}


#REGEX PATTERNS FOR OSPF CONFIGURATION## (RE.FINDALL WILL ITERATE OVER THE LINES OF THE FILE)
k1 = re.findall(r"^router ospf\s\d+", ospf, re.MULTILINE)
k2check = re.search(r"^default-information originate", ospf, re.MULTILINE)
if k2check:
 k2 = re.findall(r"^default-information originate", ospf, re.MULTILINE)
k3 = re.findall(r"^\sauto-cost\sreference-bandwidth\s\d+[10000,40000]", ospf, re.MULTILINE)
k4 = re.findall(r"(^\snetwork)\s(\d{1,3}.{1,3}.{1,3})\s(\d{1,3}.{1,3}.{1,3})\s(area\s\d{1,500})", ospf, re.MULTILINE)




#OSPF CONFIGURATION CHECK: OSPF Routing
for match in k1:
 if match >= "router ospf":
  print("OSPF is used in this configuration")
  result["OSPF_ENABLED"].append("ENABLED")

 else:
  print("OSPF is not used in this configuration")
  result["OSPF_ENABLED"].append("NOT CONFIGURED")




#OSPF CONFIGURATION CHECK: ROUTER-ID TIED TO LOOPBACK INTERFACE##
ospf_router_id = re.findall(r"^(\srouter-id).(\d{1,3}.{1,3}.{1,3}$)",ospf, re.MULTILINE)[0][1]
loopbacks = []
check = re.findall(r"interface Loopback\d{1,100}\n (:?description .+\n )?ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",ospf)
for match in check:
 loopbacks.append(match[1])

if ospf_router_id in loopbacks:
 print("ROUTER-ID is Using LoopBack Interface")
 result["ROUTER_ID"] = {'ROUTER_ID': ('BEST PRACTICE')}

else:
 print('ROUER-ID is NOT Using LoopBack Interface')
 result['ROUTER_ID'] = {'ROUTER_ID': ('NOT IN BEST PRACTICE')}






#OSPF CONFIGURATION CHECK: OSPF default-information originate
if k2check:
 for match in k2:
  if match == "default-information originate":
   print("This device generates a Default External Route into OSPF")
   result["DEFAULT_ORIGINATE"] = {'DEFAULT_ORIGINATE': ("ENABLED")}
else:
 print("This device DOES NOT generate a Default External Route into OSPF")
 result["DEFAULT_ORIGINATE"] = {'DEFAULT_ORIGINATE': ("NOT USED IN CONFIGURATION")}



#OSPF CONFIGURATION CHECK: OSPF auto-cost reference-bandwith is Greater the 10Gb##
for match in k3:
 if match >= " auto-cost reference-bandwidth 10000":
  print('OSPF auto-cost reference-bandwidth is CORRECT')
  result["REFERENCE_BANDWIDTH"] = {'REFERENCE_BANDWIDTH': ("BEST PRACTICE")}

 else:
  print("OSPF auto-cost reference-bandwidth in NOT CORRECT")
  result["REFERENCE_BANDWIDTH"] = {'REFERENCE_BANDWIDTH': ("NOT IN BEST PRACTICE")}



#OSPF Networks with Area
for match in k4:
 print(match)
 result["OSPF_NETWORKS"].append({'OSPF_NETWORKS': (match)})



print("\nOSPF CHECK RAW DATA RESULTS\n")
print(k1,k2check,k3,k4)
print("\nOSPF CHECK RESULTS\n")
print(json.dumps(result, indent=4))
