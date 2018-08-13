import csv
import operator
import pandas
from pandas import DataFrame


#Parses the RISC Raw Report "Problem Short Description" column and sorts the "Metric" column per individual Short Description item.


pandas.set_option('display.max_columns', None)
data=pandas.read_csv('Testof Core_Report_Raw.csv')

#Adds Analysis column
data['Packet Loss > 500 Packets'] = (data['Metric']>=500)


#Test to add a counting column
#data['Device Name'].value_counts()
#print(data['Device Name'].value_counts())


#data['Count_Column'] = (data['Device Name'].value_counts())
#print(data['Count_Column'].value_counts())

data.groupby('Device Name').Metric.count()
print(data.groupby)


#Sorts Metric column
data = data.sort_values(['Metric'], ascending=True)


#Removes unwanted columns on final report
data = data.drop('Category', axis=1)
data = data.drop('Core', axis=1)
data = data.drop('Problem Long Description', axis=1)
data = data.drop('Classification', axis=1)
data = data.drop('Metric Description', axis=1)

#Sets the dataframe index
data.set_index('Problem Short Description', inplace=True)

#Sets the dataframe locations for Rows to evaluate
data = data.loc[['Router Interfaces with Discards','Router Interfaces with Errors','Virtual Switch Input Packet Loss', 'Critical Uplinks with Discards', 'Shared Uplinks with Discards','Shared Uplinks with Errors']]


#print(data)

#Creates new .csv file
data.to_csv('pandatest.csv')

