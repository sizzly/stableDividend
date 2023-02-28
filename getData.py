import requests
import json
import time

xList = open("tickerlist").readlines()
List=['T.TO']
for x in List:
      time.sleep(1)
      #print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.csv'
      #print(tickerstring)
      url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&apikey=BRYEQK2HK6SPAM62&datatype=csv&symbol='
      url += x
      #print(url)

      r = requests.get(url)
      data = r.json()

      with open(tickerstring, 'w', encoding='utf-8') as f:
          f.write(response.text)
