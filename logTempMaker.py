#!/usr/bin/python

from urllib2 import urlopen
import json

token = "8boy0zr4vrm1"
dataAmount = 100
dataGet = str(5 * dataAmount)

url = 'http://dca.telefonicabeta.com/m2m/v2/services/'+token+'/assets/'+token+'/data/?sortBy=samplingTime'

jsonurl = urlopen(url)
sensorData = json.loads(jsonurl.read())
sensorData = sensorData["data"]

f = open('log_clima.txt', 'w')

auxData = sensorData[-1000:]
for data in auxData:
  if (data["ms"]["p"] == "temperature"):
    time = data["st"]
    value = str(data["ms"]["v"])
    f.write( time + ": " + value +"\n")

f.close()

