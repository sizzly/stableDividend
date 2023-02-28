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
      mean = 0
      variance = 0
      sumvariance = 0

      # Get the Average Price
      with open(tickerstring) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          line_count = 0
          for row in csv_reader:
              if line_count == 0:
                  line_count += 1
              elif line_count < 53:
                  sum52weeks = float(sum52weeks) + float(row[5])
                  line_count += 1

          print(f'Processed {line_count} lines for a total of {sum52weeks}.')
          mean = float(sum52weeks) / 52
          print(f'Mean is {sum52weeks}.')

          # Get the deviation
          variance_count = 0
          pavpi = 0
          pavpi2 = 0
          for row in csv_reader:
              if variance_count == 0:
                  variance_count += 1
              elif line_count < 53:
                  pavpi = float(row[5]) - float(mean)
                  pavpi2 = float(pavpi) * float(pavpi)
                  sumvariance = float(sumvariance) + float(pavpi2)
                  print(pavpi)
                  print(row[5])
                  variance_count += 1

          variance = float(sumvariance) / 52
          print(f'Variance is {variance}.')


# Output the 20 stocks
