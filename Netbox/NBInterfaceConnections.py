import urllib.request
import json
import csv

x = urllib.request.urlopen ("http://192.168.75.140:8000/api/dcim/interface-connections")

##print (x.read ())

data = json.load(x)

##Outputs to json format
for device in data["results"]:
  print(device["interface_a"])
  ##print (json.dumps(data, indent=2))

csvfile = open("output.csv",'a')
csvfile.close()

with open("output.csv", "w", newline='') as output:
  csv_app = csv.writer(output)
  header = "DEVICE_A", "DEVICE_A INTERFACE", "DEVICE_A INTERFACE MTU", "DEVICE_A FORM FACTOR", "CONNECTION STATUS", "DEVICE_B FORM FACTOR", "DEVICE_B INTERFACE MTU", "DEVICE_B INTERFACE", 'DEVICE_B'
  csv_app.writerow(header)

  for item in data['results']:
    row = item['interface_a']['device']['name'], item['interface_a']['name'], item['interface_a']['mtu'], item['interface_a']['form_factor']['label'], item['connection_status']['label'], item['interface_b']['form_factor']['label'], item['interface_b']['mtu'], item['interface_b']['name'], item['interface_b']['device']['name']
    csv_app.writerow(row)

#for item in data['results']:
 # name = item['name']
 # print(name)



