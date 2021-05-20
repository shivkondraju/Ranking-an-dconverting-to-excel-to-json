
import pandas as pd
import csv,json
data=pd.read_excel('game_user_sample.xlsx',index_col=None)
data['diff']=data['games_played']-data['games_won']
data['rank']=data['diff'].rank(method='first',ascending=True)
data=data.sort_values('rank')

data.to_csv('out.csv',index=False)
dataJson={}
with open('out.csv') as csvFile:
  csvReader=csv.DictReader(csvFile)
  for csvRow in csvReader:
    user_name=csvRow['user_name']
    dataJson[user_name]=csvRow

with open('jsonFile.json','w') as jsonFile:
  jsonFile.write(json.dumps(dataJson,indent=4))
