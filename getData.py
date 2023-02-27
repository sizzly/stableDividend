import requests
import json
import time

thislist = ["T.TO", "MFC.TO", "CU.TO", "SLF.TO", "IGM.TO", "BCE.TO", "ENB.TO", "ALA.TO", "LIF.TO", "GEI.TO"]
for x in thislist:
      time.sleep(2)
      print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.data'
      print(tickerstring)
      url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&apikey=BRYEQK2HK6SPAM62&symbol='
      url += x
      print(url)

  #r = requests.get(url)
  #data = r.json()

  #with open(tickerstring, 'w', encoding='utf-8') as f:
#      json.dump(data, f, ensure_ascii=False, indent=4)
