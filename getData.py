import requests
import time

List = open("tickerlist").readlines()
#List=['T.TO', 'ALA.TO']
for x in List:
      time.sleep(15)
      #print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.csv'
      tickerstring = str(tickerstring)
      #print(tickerstring)
      url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&apikey=BRYEQK2HK6SPAM62&datatype=csv&symbol='
      url += x
      #print(url)

      response = requests.get(url)

      with open(tickerstring, 'w', encoding='utf-8') as f:
          f.write(response.text)
