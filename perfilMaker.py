#!/usr/bin/python

from src import *


""" calcular vendas do dia = mediaVendaTempo * tempoTrabalho(segundos) """

tempoTrabalho = 3600 # tempo de trabalho

mimTemp = 15
maxTemp = 43


def mediaVendasTempo(mimTemp, maxTemp, logClima, logVendas, relacao):
  """ Calcula a relacao de vendas por tempo"""
  tempoTotal = getTempo(logClima[-1]) - getTempo(logClima[0])
  qtdVendas = calcVendasTotais(logVendas)
  
  media = float(qtdVendas) / tempoTotal
  return media

def relacaoVendasTemperatura(mimTemp, maxTemp, logClima, logVendas):
  """ Calcula a relacao de vendas por temperatura """
  qtdTemperatura = dict((i,0) for i in range(mimTemp,maxTemp))
  nVendas = dict((i,0) for i in range(mimTemp,maxTemp))
  relacao = dict((i,None) for i in range(mimTemp,maxTemp))

  for linhaClima in logClima:
    time = linhaClima.split(': ')[0] #pega a data
    temperatura = float(linhaClima.split(': ')[1][:-1])
    qtdTemperatura[temperatura] += 1

    for linhaVendas in logVendas:
      if time in linhaVendas:
        qtd = int(linhaVendas.split(': ')[1][:-1])
        nVendas[temperatura] += qtd


  for temp in range(mimTemp, maxTemp):
    qtd = qtdTemperatura[temp]
    vendidos = nVendas[temp]
    if qtd != 0:
      relacao[temp] = float(vendidos)/qtd

  return relacao


f = open("log_clima.txt", "r")
logClima = f.readlines()
f.close()

f = open("log_vendas.txt", "r")
logVendas = f.readlines()
f.close()

f = open("perfil.txt", "w")

relacao = relacaoVendasTemperatura(mimTemp, maxTemp, logClima, logVendas)

for temp in range(mimTemp, maxTemp):
  if relacao[temp] != None:
    f.write(str(temp) + ': ' + str(relacao[temp]) + '\n')

f.close()

relacaoUnit = relacaoUnitaria(relacao)
print relacaoUnit

media = mediaVendasTempo(mimTemp, maxTemp, logClima, logVendas, relacao)

previsao = {}
for temp in relacaoUnit.keys():
  previsao[temp] = media*tempoTrabalho*relacaoUnit[temp]

f = open("previsao.txt", "w")
for temp in sorted(previsao.keys()):
  f.write(str(temp) + ': ' + str(previsao[temp]) + '\n')

f.close()
