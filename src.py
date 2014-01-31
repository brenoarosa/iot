#!/usr/bin/python

import collections

def transform(data):
  """ transformar data no formato 2014-01-28T21:04:45Z em segundos """
  calendario = data.split('T')[0]
  horario = data.split('T')[1][:-1]

  segundo = int(horario.split(':')[2])
  minuto = int(horario.split(':')[1])
  hora = int(horario.split(':')[0])
  dia = int(calendario.split('-')[2])
  mes = int(calendario.split('-')[1])

  resultado = (segundo + 60*minuto + 60*60*hora + 24*60*60*dia + 30*24*60*60*mes)
  return resultado

def getTempoTotal(dataInicial, dataFinal):
  """ subtrai os dois tempos para achar o tempo total """
  return ( transform(dataFinal) - transform(dataInicial) )

def getTemperatura(linhaLog):
  """ pega a temperatura de uma linha do log"""
  temp = float(linhaLog.split(': ')[1])
  return temp

def getTempo(linhaLog):
  """ pega o tempo de uma linha do log"""
  tempo = transform(linhaLog.split(': ')[0])
  return tempo

def calcVendasTotais(logVendas):

  qtd = 0
  for linhaVendas in logVendas:
    qtd += int(linhaVendas.split(': ')[1][:-1])

  return qtd

def tempMedia(relacao):

  aux = {}
  for key in relacao.keys():
    if relacao[key] == None:
      pass
    else:
      aux[key] = relacao[key]

  nTemps = 0
  total = 0

  for key in aux.keys():
    nTemps += 1
    total += key

  media = total / nTemps
  return media

def relacaoUnitaria(relacao):
  temperaturaMedia = tempMedia(relacao)
  aux = {}
  valor = 1.0 / relacao[temperaturaMedia] 
  
  for key in relacao.keys():
    if relacao[key] == None:
      pass
    else:
      aux[key] = relacao[key] * valor 
  
  return aux

def calcDuracaoTemperaturas(mimTemp, maxTemp, logClima):
  
  duracaoTemp = dict((i,0) for i in range(mimTemp,maxTemp))
  tempAux = getTemperatura(logClima[0])
  horaAux = getTempo(logClima[0])
  mudou = False # contorna o erro se todo log estiver na mesma temperatura

  for linhaLog in logClima:
    tempAtual = getTemperatura(linhaLog)
    horaAtual = getTempo(linhaLog)

    if tempAtual != tempAux:
      print str(tempAux) +': '+ str(horaAtual) +' '+str(horaAux)+' '+ str(horaAtual - horaAux)
      duracaoTemp[tempAux] += horaAtual - horaAux
      horaAux = horaAtual
      tempAux = tempAtual
      mudou = True

  if mudou == False:
    duracaoTemp[tempAux] = getTempoTotal(logClima[0].split(': ')[0], logClima[-1].split(': ')[0])

  return duracaoTemp
