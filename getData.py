import requests
import json
import time

thislist = ["T.TO", "MFC.TO", "CU.TO", "SLF.TO", "IGM.TO", "BCE.TO", "ENB.TO", "ALA.TO", "LIF.TO", "GEI.TO"]
for x in thislist:
  print(x)
  tickerstring = './data/'
  tickerstring += x
  tickerstring += '.data'
  print(tickerstring)
  #time.sleep(15)
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=T.TO&apikey=BRYEQK2HK6SPAM62'
#r = requests.get(url)
#data = r.json()

#with open('./data/t.to.data', 'w', encoding='utf-8') as f:
#        json.dump(data, f, ensure_ascii=False, indent=4)
