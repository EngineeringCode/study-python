import requests
import urllib.parse
import datetime
import pandas

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
serviceKey = ""
serviceKeyDecoded = urllib.parse.unquote(serviceKey, 'UTF-8')
pageNo = '1'
numOfRows = '1000'
dataType = 'JSON'
base_date = datetime.datetime.now().strftime('%Y%m%d')
base_time = datetime.datetime.now().strftime('%H') + '00'
nx = '86' # 구미시 산동읍
ny = '97' # 구미시 산동읍

params ={'serviceKey' : serviceKeyDecoded,
         'pageNo' : pageNo,
         'numOfRows' : numOfRows,
         'dataType' : dataType,
         'base_date' : base_date,
         'base_time' : base_time,
         'nx' : nx,
         'ny' : ny }

response = requests.get(url, params=params)

print(response.content)

data = response.json()
df = pandas.json_normalize(data['response']['body']['items']['item'])

print(df)