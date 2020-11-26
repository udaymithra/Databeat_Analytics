import pandas as pd
import csv
datafile=pd.read_csv('data.csv')
datafile.shape
datafile.head(3)
datafile.info()
datafile.columns
activity_datafile=pd.read_csv('activity_data.csv')
activity_datafile.shape
activity_datafile.head()
activity_datafile.info()
activity_datafile.columns
outputfile=pd.read_csv('output.csv')
outputfile.shape
outputfile.info()
outputfile.columns
series_of_ids=datafile['_id']
outputfile['id']=series_of_ids
outputfile.head()
output_final=pd.merge(outputfile,activity_datafile,on='id')
final_output_csv_file=output_final.to_csv()
