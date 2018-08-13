import pandas
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

pandas.set_option('display.max_columns', None)
data=pandas.read_csv('Testof Core_Report_Raw.csv')


data = data.sort_values(['Category','Problem Short Description', 'Metric'], ascending=True)
#Creating Subset of Columns
#subset = data[['Problem Short Description','Device Name','Metric']]
#print(subset)
#grouped = data.groupby('Device Name')['Problem Short Description'].count()
#print(grouped)

#Removes unwanted columns on final report
data = data.drop('Core', axis=1)
data = data.drop('Problem Long Description', axis=1)
data = data.drop('Classification', axis=1)
#data = data.drop('Metric Description', axis=1)


print(data)
data.to_csv('pandatest2.csv')


