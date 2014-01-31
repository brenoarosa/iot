#!/usr/bin/python

import random

f = open("log_clima.txt", "r")
logClima = f.readlines()
f.close()

f = open("log_vendas.txt", "w")

tempMax = 0
tempMin = 100

for linha in logClima:
  temp = float(linha.split(": ")[1][:-1])
  if temp > tempMax:
    tempMax = temp
  if temp < tempMin:
    tempMin = temp

tempMedia = tempMax + tempMin
tempMedia = tempMedia/2

for linha in logClima:
  time = linha.split(': ')[0] #pega a data
  temp = float(linha.split(": ")[1][:-1])
  if (random.randint(tempMin,tempMax) + random.randint(tempMin,tempMax) + random.randint(tempMin,tempMax) + temp*2> 5*tempMedia ): #sorteia certa quantidade de horas registradas para existir uma venda
    qtd = str(random.randint(1,3)) #sorteia uma quantidade
    f.write( time + ": " + qtd +"\n")
  
f.close()

