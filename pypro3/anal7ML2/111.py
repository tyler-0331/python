import requests
import xmltodict
import pandas as pd

url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
params ={'serviceKey' : 'x+wB0jStYlKe8vROEBp+XGXpIXAMHSzYaDWZ6DEciNEfl3ypAAvQwkFXN/cnZ67xg+mr13V9TZjeRT7Xkog4rg==', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201612' }

resp = requests.get(url, params=params)
print(resp.content.decode('utf-8'))
print()
data = xmltodict.parse(resp.content.decode('utf-8'))
print(data)
print()
print(data['response']['body']['items']['item'])
print()
print(pd.DataFrame(data['response']['body']['items']['item']))
