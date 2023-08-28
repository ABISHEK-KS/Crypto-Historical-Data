import pandas as pd
import pandas_profiling as pp
filedata=pd.read_excel("Combined.xlsx")
profilereport=pp.ProfileReport(filedata)
profilereport.to_file("index.html")
print(filedata.info())
print('-------------------------------')
print(filedata.describe())