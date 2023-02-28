# Crunch Numbers
#
# Generates a list of 20 stocks that match the Stable Dividend Portfolio
# It's a way to get the annual volatility value which most stock screeners do
# not provide.

# Load up each of the ticker datafiles
import csv

List=['T.TO']
for x in List:
      #print(x)
      tickerstring = './data/monthly_adjusted_'
      tickerstring += x
      tickerstring += '.csv'
      print(tickerstring)

      sum52weeks = 0

      with open(tickerstring) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          line_count = 0
          for row in csv_reader:
              if line_count == 0:
                  line_count += 1
              elif line_count < 53:
                  sum52weeks = float(sum52weeks) + float(row[5])
                  print(f'\t{row[5]}')
                  line_count += 1

          print(f'Processed {line_count} lines for a total of {sum52weeks}.')

# Output the 20 stocks
