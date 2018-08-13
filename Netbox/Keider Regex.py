
import sys
import re
import json



with open('bucketsnort.txt', 'r') as f:
    f_contents = f.read()
    #print(f_contents)
    # The Results Dictionary for JSON Output
    result = {
            "features": [],
            "interfaces_IP": {},
            "interfaces_description": {}
    }


 # check if OSPF is used as the routing protocol

# the following regex_pattern matches only the "router ospf <process-id>" command (no VRFs)
ospf_regex_pattern = r"^router ospf \d+$"

 # we will use the re.search() function, because the re.match() function ignores the MULTILINE flag
# if the command is not found, the return value is None
is_ospf_in_use = True if re.search(ospf_regex_pattern, f_contents, re.MULTILINE) else False

if is_ospf_in_use:
    print("==> OSPF is used in this configuration")
    result["features"].append("OSPF")

else:
    print("==> OSPF is not used in this configuration")




# extract the interface name
interface_descriptions = re.finditer(r"^(interface (?P<intf_name>\S+))\n" r"( .*\n)*", f_contents, re.MULTILINE)

for intf_part in interface_descriptions:
    print ("Found Interface: '%s'" % (intf_part.group("intf_name")))
    result["interfaces_description"][intf_part.group("intf_name")] = {"interface": intf_part.group("intf_name")}



# extract the IPv4 address of the interfaces
interface_ips = re.finditer(r"^(interface (?P<intf_name>.*)\n)" r"( .*\n)*" r"( ip address (?P<ipv4_address>\S+) (?P<subnet_mask>\S+))\n", f_contents, re.MULTILINE)

for intf_ip in interface_ips:
   print("==> found interface '%s' with ip '%s/%s'" % (intf_ip.group("intf_name"), intf_ip.group("ipv4_address"), intf_ip.group("subnet_mask")))

   result["interfaces_IP"][intf_ip.group("intf_name")] = {"ipv4_address": intf_ip.group("ipv4_address")},{"subnet_mask": intf_ip.group("subnet_mask")}


print("\nEXTRACTED PARAMETERS\n")
print(json.dumps(result, indent=4))



