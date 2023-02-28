# Crunch Numbers
#
# Generates a list of 20 stocks that match the Stable Dividend Portfolio
# It's a way to get the annual volatility value which most stock screeners do
# not provide.

# Load up each of the ticker datafiles
import json

List=['T.TO']
for x in List:
      #print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.data'
      print(tickerstring)

      with open(tickerstring, 'r') as ticker_file:
          ticker_data = json.load(ticker_file)
          print(ticker_data["Weekly Adjusted Time Series"]["2023-02-24"]["5. adjusted close"]); \
          print(ticker_data["Weekly Adjusted Time Series"]["2023-02-17"]["5. adjusted close"])

# Output the 20 stocks
