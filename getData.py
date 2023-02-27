import requests
import json
import time

List = open("tickerlist").readlines()
for x in List:
      #time.sleep(15)
      print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.data'
      print(tickerstring)
      url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&apikey=BRYEQK2HK6SPAM62&symbol='
      url += x
      print(url)
