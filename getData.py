import requests
import time

#List = open("tickerlist").readlines()
List=['TF.TO', 'RY.TO', 'RSI.TO', 'ACO-X.TO', 'CF.TO', 'AFN.TO', 'ALS.TO', 'FEC.TO', 'CAS.TO', 'SIS.TO', 'BDGI.TO', 'ASTL.TO', 'NBLY.TO', 'MRE.TO', 'EFX.TO', 'CJ.TO', 'SII.TO', 'DRM.TO', 'DND.TO', 'AOI.TO', 'UNC.TO', 'PSI.TO', 'CVG.TO', 'MRC.TO', 'LNF.TO', 'TCLb.TO', 'MTL.TO', 'LB.TO', 'WTE.TO', 'MTY.TO', 'HCG.TO', 'DPM.TO', 'NWC.TO', 'HBM.TO', 'CG.TO', 'OGC.TO', 'CEE.TO', 'SSL.TO', 'GSY.TO', 'CJT.TO', 'UNS.TO', 'PEY.TO', 'AND.TO', 'EIF.TO', 'FR.TO', 'RUS.TO', 'SPB.TO', 'BIR.TO', 'RCH.TO', 'LIF.TO', 'ENGH.TO', 'FN.TO', 'FRU.TO', 'TVE.TO', 'PRU.TO', 'PXT.TO', 'SVI.TO', 'EQB.TO', 'SES.TO', 'CWB.TO', 'WPK.TO', 'TPZ.TO', 'CIX.TO', 'SJ.TO', 'STLC.TO', 'INE.TO', 'PET.TO', 'TA.TO', 'VET.TO', 'TCN.TO', 'RNW.TO', 'CCA.TO', 'ELF.TO', 'OR.TO', 'LUG.TO', 'PRMW.TO', 'MFI.TO', 'GEI.TO', 'CIA.TO', 'BLX.TO', 'SSRM.TO', 'PAAS.TO', 'DFY.TO', 'POU.TO', 'PBH.TO', 'LNR.TO', 'MX.TO', 'ERF.TO', 'SNC.TO', 'BTO.TO', 'CPX.TO', 'FTT.TO', 'PSK.TO', 'CPG.TO', 'PKI.TO', 'AGI.TO', 'ONEX.TO', 'LUN.TO', 'WCP.TO', 'ALA.TO', 'CIGI.TO', 'EDV.TO', 'KEY.TO', 'AQN.TO', 'X.TO', 'GIL.TO', 'EFN.TO', 'NPI.TO', 'FSV.TO', 'WFG.TO', 'STN.TO', 'RBA.TO', 'DOO.TO', 'TIH.TO', 'IAG.TO', 'ARX.TO', 'CAE.TO', 'CU.TO', 'IGM.TO', 'OTEX.TO', 'BEPC.TO', 'FM.TO', 'GFL.TO', 'TFII.TO', 'EMA.TO', 'SAP.TO', 'MRU.TO', 'NCM.TO', 'CTC.TO', 'TOU.TO', 'H.TO', 'WSP.TO', 'MG.TO', 'DOL.TO', 'FFH.TO', 'WN.TO', 'POW.TO', 'PPL.TO', 'WPM.TO', 'FTS.TO', 'QSR.TO', 'AEM.TO', 'FNV.TO', 'NA.TO', 'GWO.TO', 'IFC.TO', 'L.TO', 'T.TO', 'SLF.TO', 'IMO.TO', 'NGT.TO', 'WCN.TO', 'CVE.TO', 'CSU.TO', 'NTR.TO', 'BCE.TO', 'TRP.TO', 'CM.TO', 'ATD.TO', 'ENB.TO', 'BN.TO', 'TRI.TO', 'BNS.TO', 'CNQ.TO', 'BMO.TO', 'CP.TO', 'TD.TO']
for x in List:
      time.sleep(15)
      #print(x)
      tickerstring = './data/'
      tickerstring += x
      tickerstring += '.csv'

      #print(tickerstring)
      url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&apikey=BRYEQK2HK6SPAM62&datatype=csv&symbol='
      url += x
      #print(url)

      response = requests.get(url)

      with open(tickerstring, 'w', encoding='utf-8') as f:
          f.write(response.text)
