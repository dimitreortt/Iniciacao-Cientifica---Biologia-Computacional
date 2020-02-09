from random import randint
from collections import Counter
import copy
import os
from time import time, ctime
import sys
sys.path.insert(0, '../')
#import geraLosangoOperations
#dadas duas listas de posicoes, como eu encontro todos os geneMatchings possiveis

def getFmly(genoma):
	fmly = {}
	# create dictionary {gene family : positions of family in genome}
	for idx, itm in enumerate(genoma):
	    if(itm not in fmly):
	        fmly[itm] = [idx]
	    else:
	        fmly[itm].extend([idx])

	return fmly
# Essa funcao retorna uma lista de tamanho 6(no topo da recursao claro...)
def collectAllGeneMatchings(lista1, lista2):
	#print 'Executing CollectAllGeneMatchings...' 
	
	if lista1 == [] or lista2 == []:
		return [[]]

	listaAll = []
	#travasPossiveis lista todas as travas possiveis para o primeiro elemento
	#da lista1
	travasPossiveis = [(lista1[0], item) for item in lista2]
	for item in travasPossiveis:

		l1,l2 = copy.deepcopy(lista1), copy.deepcopy(lista2)
		l1.remove(item[0])
		l2.remove(item[1])

		listaHere = collectAllGeneMatchings(l1, l2)
		for lista in listaHere:
			lista.insert(0, item)
		listaAll.extend(listaHere)

	return listaAll

def sameContent(inp, ent):
   if Counter(inp) == Counter(ent): 
      return True
   else: 
      return False


def updateMedia(time):
	mystruc = getNumberOfCommonIntervals.struc
	mystruc[0] += time
	mystruc[1] += 1

	print ('media: %f\n' % (mystruc[0]/float(mystruc[1])))
	getNumberOfCommonIntervals.struc = mystruc

# remove da lista as posicoes estrategicamente vazias
def fixRange(lista):
	for idx, i in reversed(list(enumerate(lista))):
		if i == '':
			lista.pop(idx)
	return lista

#listOfMatchings eh um MM
def getStrings(listOfMatchings):

	a = len(listOfMatchings)
	
	# inicializa listas para a recuperacao das strings correspondentes
	# aos genomas
	cpy1 = ['' for i in range(a)]
	cpy2 = ['' for i in range(a)]

	#print 'listOfMatchings: %r' % listOfMatchings
	
	# para cada mapeamento faca:
	for i in listOfMatchings:
		# copiaGenoma[pos] = nomeGene
		pos_g1, pos_g2, geneId = i[0], i[1],i[0]
		cpy1[pos_g1] = geneId
		cpy2[pos_g2] = geneId

	# corrige alcances (posicoes) dos genes apos filtragem 
	# que remove genes imapeaveis - fixRange()
	cpy1 = fixRange(cpy1)
	cpy2 = fixRange(cpy2)

	return cpy1, cpy2	

def recoverStrings(MM):
	gatherList = []
	for matching in MM:
		gatherList.extend(matching)

	# cpy1 e cpy2 recebem as strings correspondentes ao matching realizado, com os genes
	# que nao sao mapeados sendo removidos	
	cpy1, cpy2 = getStrings(gatherList)
	
	# chrList recebe a lista com os nomes dos genomas traduzida para uma lista
	# com identificadores unicos, atraves do metodo unichr()
	chrList1 = [unichr(int(item)) for item in cpy1]
	chrList2 = [unichr(int(item)) for item in cpy2]

	return ''.join(chrList1), ''.join(chrList2)

def getOutfileLines(pathToOutput):
	
	if getOutfileLines.count == 0:
		getOutfileLines.count = 1
		outFile = open(pathToOutput, 'w')
		outFile.close()
	
	outFile = open(pathToOutput, 'r')
	outFileLines = [item.split() for item in outFile.readlines()]
	outFile.close()

	if getOutfileLines.count == 100:
		getOutfileLines.count = 1
		print ("%r" % ({int(item[0]):int(item[1]) for item in outFileLines}))
	else:
		getOutfileLines.count += 1

	return outFileLines
getOutfileLines.count = 0

def getOutPath():
	outPutPath = os.getcwd().replace('drivers/geraLosango', 'saidas/losangos/')
	outName = sys.argv[1] + '_losango'

	return outPutPath + outName

def getGlobalFmly(lst):
	gFmly = {}
	for item in lst:
		a, b = item[0], item[1]
		gFmly[int(a)] = int(b)
	
	return gFmly

def updateGlobalResults(pathToOutput, localFmly, outFileLines):
	
	globalFmly = getGlobalFmly(outFileLines)
	for item in localFmly:
		qtd = len(localFmly[item])

		name = item
		if name in globalFmly:
			globalFmly[name] += qtd
		else:			
			globalFmly[name] = qtd

	outFile = open(pathToOutput, 'w')

	for i in globalFmly:
		qtdPresences = globalFmly[i]
		outFile.write("%d\t%d\n" % (i, qtdPresences))

def calculationDriver(inputName):
	myFile = open(inputName+'_quadroSaida', 'r')
	lines = myFile.readlines()

	# results armazena os valores das saidas contidas em genomaX_quadroSaida
	localResults = [int(item.split('\n')[0]) for item in lines[6::3]]

	localFmly = getFmly(localResults)

	pathToOutput = getOutPath()
	outFileLines = getOutfileLines(pathToOutput)

	updateGlobalResults(pathToOutput, localFmly, outFileLines)

def generateOutput(listOfMM, numberGenome, genoma1, genoma2):
	#print listOfMM, numberGenome, genoma1, genoma2
	#print os.getcwd()
	#exit()
	outPutFile = open(numberGenome+'_quadroSaida', 'w')
	outPutFile.write('genomas:\n%s\n%s\n\n' % (genoma1, genoma2))

	outPutFileVerbose = open(numberGenome+'_quadroSaida_verbose', 'w')
	outPutFileVerbose.write('genomas:\n%s\n%s\n\n' % (genoma1, genoma2))
	outPutFileVerbose.write('Maximum Matching;\nString1\nString2\nList Of Common Intervals\nNumber Of Common Intervals\n\n')

	# para cada Maximum Matching na lista de Todos os Maximum Matchings
	# existentes para esse genoma faca:
	for MM in listOfMM:
		strG1, strG2 = recoverStrings(MM)
		numCIs, listOfCIs = getNumberOfCommonIntervals(strG1, strG2)

		# escreve na saida simplificada
		outPutFile.write('%r\n%d\n\n' % (MM, numCIs))

		#escreve na saida (verbose)
		outPutFileVerbose.write("%r\n%r\n%r\n%r\n%d\n\n" % (MM,strG1,strG2,listOfCIs,numCIs))
