import sys
import pandas as pd
import re
from influxdb_client import InfluxDBClient

client = InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org")

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
                names=['datum','Lufttemperatur','Feuchtigkeit Temperatur','Kompost temp1','Kompost temp2','Kompost temp3','Zuluft Temperatur','CO2','Temperatur draussen','Feucht temp draussen','CO2 draussen','Trocknen','Desinfektion','RF Zuluft','Zuluft Temperatur unit','Zuluft Feucht temp','Luftklappe','Kuehlung','Heizung','Befeuchtigung','Ventilator','Dampf','Licht','Kuehlung Pumpe','Vorheizung','Vorbefeuchtigung','Kompost sw','Lufttemperatur sw','Zuluft sw','CO2 sw','RF-AF-FD sw','CO2 min','CO2 max','Abs Feucht Zuluft sw','Vorheizung temp sw','Kompost durch','Kompost diff','RF Luft','AF Luft','FD Luft','Absolute Feucht Maximum','Absolute Feucht Minimum','Misch luft','RF draussen','AF draussen','AF Zuluft','FD Zuluft','Entalpie Raum','Entalpie draussen','Sauerstoff','Phase'])
df = df.iloc[:,[0,1,6,7,10,14,16,17,18,20,21,24,49,50]]
df[df.duplicated(keep=False)]



db = 'Gicompar'+room+''

timeValues.index  = df[ ['datum'] ]
tags = {'Lufttemperatur': df[['Lufttemperatur']], 'Zuluft Temperatur': df[['Zuluft Temperatur']], 'CO2':df[['CO2']]}

client.switch_database('db')
client.write_points(db, tbName, timeValues, tags = tags)
