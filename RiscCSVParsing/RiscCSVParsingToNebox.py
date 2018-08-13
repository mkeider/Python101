

### Reads in the RISC Networks Asset Report, parses Hostname, Model, and Serial Number. Creates CSV for import into NetBox for Devices ###

import csv

#Open CSV File in Memory#
with open('RiscAsset.csv', 'r', encoding="utf_8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

#Create new CSV File#
    with open('riscparsed.csv', 'w') as new_file:
        fieldnames = ['Hostname', 'Model', 'Serial Number']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()
#Delete unwanted Headers#
        for line in csv_reader:
            del line['\ufeffDevice IP']
            del line['RAM']
            del line['Description']
            csv_writer.writerow(line)

    #for line in csv_reader:
     #   print(line)
