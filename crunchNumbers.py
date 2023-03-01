# Crunch Numbers
#
# Generates a list of 20 stocks that match the Stable Dividend Portfolio
# It's a way to get the annual volatility value which most free stock screeners
# do not provide.

import csv
import math
import statistics

f = open("volatility.csv", "w")
f.write('Ticker,Volatility,Annual Volatility\n')
f.close()

# Load up each of the ticker datafiles
#List = open("tickerlist").readlines()
List=['TF.TO', 'RY.TO', 'RSI.TO', 'ACO-X.TO', 'CF.TO', 'AFN.TO', 'ALS.TO', 'FEC.TO', 'CAS.TO', 'SIS.TO', 'BDGI.TO', 'ASTL.TO', 'NBLY.TO', 'MRE.TO', 'EFX.TO', 'CJ.TO', 'SII.TO', 'DRM.TO', 'DND.TO', 'AOI.TO', 'UNC.TO', 'PSI.TO', 'CVG.TO', 'MRC.TO', 'LNF.TO', 'TCLb.TO', 'MTL.TO', 'LB.TO', 'WTE.TO', 'MTY.TO', 'HCG.TO', 'DPM.TO', 'NWC.TO', 'HBM.TO', 'CG.TO', 'OGC.TO', 'CEE.TO', 'SSL.TO', 'GSY.TO', 'CJT.TO', 'UNS.TO', 'PEY.TO', 'AND.TO', 'EIF.TO', 'FR.TO', 'RUS.TO', 'SPB.TO', 'BIR.TO', 'RCH.TO', 'LIF.TO', 'ENGH.TO', 'FN.TO', 'FRU.TO', 'TVE.TO', 'PRU.TO', 'PXT.TO', 'SVI.TO', 'EQB.TO', 'SES.TO', 'CWB.TO', 'WPK.TO', 'TPZ.TO', 'CIX.TO', 'SJ.TO', 'STLC.TO', 'INE.TO', 'PET.TO', 'TA.TO', 'VET.TO', 'TCN.TO', 'RNW.TO', 'CCA.TO', 'ELF.TO', 'OR.TO', 'LUG.TO', 'PRMW.TO', 'MFI.TO', 'GEI.TO', 'CIA.TO', 'BLX.TO', 'SSRM.TO', 'PAAS.TO', 'DFY.TO', 'POU.TO', 'PBH.TO', 'LNR.TO', 'MX.TO', 'ERF.TO', 'SNC.TO', 'BTO.TO', 'CPX.TO', 'FTT.TO', 'PSK.TO', 'CPG.TO', 'PKI.TO', 'AGI.TO', 'ONEX.TO', 'LUN.TO', 'WCP.TO', 'ALA.TO', 'CIGI.TO', 'EDV.TO', 'KEY.TO', 'AQN.TO', 'X.TO', 'GIL.TO', 'EFN.TO', 'NPI.TO', 'FSV.TO', 'WFG.TO', 'STN.TO', 'RBA.TO', 'DOO.TO', 'TIH.TO', 'IAG.TO', 'ARX.TO', 'CAE.TO', 'CU.TO', 'IGM.TO', 'OTEX.TO', 'BEPC.TO', 'FM.TO', 'GFL.TO', 'TFII.TO', 'EMA.TO', 'SAP.TO', 'MRU.TO', 'NCM.TO', 'CTC.TO', 'TOU.TO', 'H.TO', 'WSP.TO', 'MG.TO', 'DOL.TO', 'FFH.TO', 'WN.TO', 'POW.TO', 'PPL.TO', 'WPM.TO', 'FTS.TO', 'QSR.TO', 'AEM.TO', 'FNV.TO', 'NA.TO', 'GWO.TO', 'IFC.TO', 'L.TO', 'T.TO', 'SLF.TO', 'IMO.TO', 'NGT.TO', 'WCN.TO', 'CVE.TO', 'CSU.TO', 'NTR.TO', 'BCE.TO', 'TRP.TO', 'CM.TO', 'ATD.TO', 'ENB.TO', 'BN.TO', 'TRI.TO', 'BNS.TO', 'CNQ.TO', 'BMO.TO', 'CP.TO', 'TD.TO']

for x in List:
      #print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.csv'
      print(tickerstring)

      change_list = []
      volatility =0
      annualVolatility = 0
      preceeding_price = 0

      # Get the Average Price
      with open(tickerstring) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=',')
          line_count = 0
          for row in csv_reader:
              if line_count == 0:
                  line_count += 1
              elif line_count == 1:
                  # record closing price
                  preceeding_price = row[5]
                  # increment line_count
                  line_count += 1
              elif line_count < 262:
                  # calculate % change
                  change = float(preceeding_price) - float(row[5])
                  percent_change = float(change) / float(row[5])

                  # Add to change_list
                  change_list.append(percent_change)

                  #record closing Price
                  preceeding_price = row[5]
                  #increment line_count
                  line_count += 1

          #calculate volatility & annual volatility
          volatility = statistics.stdev(change_list)

          annualVolatility = math.sqrt(260) * float(volatility)

          #write them to a CSV
          f = open("volatility.csv", "a")
          f.write(f'{x},{volatility},{annualVolatility}\n')
          f.close()
