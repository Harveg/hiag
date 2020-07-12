import sys
import pandas as pd
import re
from Influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, username='admin', password='')

if len(sys.argv) < 1:
    print("Missing argument")
    exit()

room = re.sub("LOT\d{4}", "", sys.argv[1])
print("Room Nr: "+room)

try:
    roomint = int(room)
except ValueError:
    print("Illegal LOT-Nr: "+sys.argv[1])
    exit()

if roomint < 0 or roomint > 15:
    print("Illegal Room Nr.")
    exit()

df = pd.read_csv('/etc/openhab2/scripts/grafiek'+room+'.dat',
                 header=None,
                 skiprows = 1,
                 encoding='ISO-8859-1',
                 names=['datum','Lufttemperatur','Feuchtigkeit Temperatur','Kompost temp1','Kompost temp2','Kompost tem$
df1 = df.iloc[:,[0,1,6,7,10,14,16,17,18,20,21,24,49,50]]
df1[df.duplicated(keep=False)]



db = Gicompar++room++

timeValues.index  = df[ ['datum'] ]
tags = {'Lufttemperatur': df[['Lufttemperatur']], 'Zuluft Temperatur': df[['Zuluft Temperatur']], 'CO2':df[['CO2']]}

client.switch_database('db')
client.write_points(db, tbName, timeValues, tags = tags)
