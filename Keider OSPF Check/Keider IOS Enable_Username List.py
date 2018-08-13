import re
import csv
import json
import os.path


#Script is for LEGACY CISCO IOS

#This script checks the configuration file for: Enable Secret, Enable Password, and Username. Then write the list to .csv file (authlist.csv)



#Configuration Snippet used for Testing
UserIOS = '''
IOS CONFIGS
hostname Router
enable secret 5 $1$D5P6$PYx41/lQIASK.HcSbfO5q1 
enable password xxxxxx 
username username1 password 0 kV9sIj3 

'''


result = {
 "IosHostname": [],
 "IosEnableSecret": [],
 "IosEnablePwd": [],
 "IosUsername": [],

}


#Cisco IOS REGEX Patterns
IosHostname = re.findall(r"^(hostname)\s(.\S+)", UserIOS, re.MULTILINE)
for match in IosHostname:
    print(match[1])
    result["IosHostname"].append(match[1])

IosEnableSecret = re.findall(r"^(enable\ssecret\s\d{1,16}\s.\S+)",UserIOS, re.MULTILINE)
for match in IosEnableSecret:
    print(match)
    result["IosEnableSecret"].append(match)

IosEnablePwd = re.findall(r"^(enable\spassword\s.\S+)", UserIOS, re.MULTILINE)
for match in IosEnablePwd:
    print(match)
    result['IosEnablePwd'].append(match)

IosUsername = re.findall(r"^(username\s\S+\spassword\s\d{1,20}\s.\S+)", UserIOS, re.MULTILINE)
for match in IosUsername:
    print(match)
    result['IosUsername'].append(match)


#Print IOS Enable and Usernames to appended CSV File
file_exists = os.path.isfile("authlist.csv")
with open('authlist.csv', 'a', newline='') as new_file:
    fieldnames = ['IosHostname', 'IosEnableSecret', 'IosEnablePwd', 'IosUsername']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    if not file_exists:
        csv_writer.writeheader()#If File Does Not Exist, Write the Header

    for line in [result]:
        csv_writer.writerow(line)






print(json.dumps(result, indent=4))