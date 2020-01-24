import requests
import json

url = 'http://www.gaitameonline.com/rateaj/getrate'

response = requests.get(url)

#response.json()でJSONデータに変換して変数へ保存
jsonData = response.json()

print(jsonData)

usdjpy = [i for i in jsonData['quotes'] if i["currencyPairCode"] == "USDJPY"]

if len(usdjpy) > 0:
    print(usdjpy[0]['ask'])
    print(usdjpy[0]['bid'])