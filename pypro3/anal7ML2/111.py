import requests

print(requests.get('http://openapi.seoul.go.kr:8088/6662437a4274796c36344179514c6a/xml/OpenAptInfo/1/5/').content)

