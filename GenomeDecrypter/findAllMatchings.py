'''genes = range(1,4)

para todas as possibilidades do gene 1:
	#encontre todas as possibilidades de todos os outros genes
	para todas as possibilidades do gene 2:
		encontre todas as possibilidades do gene 3
		imprima o matching #use 3a 3b 3c pra ficar mais facil de visualizar (ao invez de 4,5,6 sla kkk.....)

---Possivel maneira:-----
Para cada gene, fazer uma lista com todos os matchings possiveis'''
import sys
import os
from CollectGeneMatchings import collectAllGeneMatchings as cm
from CollectGeneMatchings import recoverStrings
#from modeOne import modeOne
import copy

import time
import os
import subprocess as sp

'''--------CollectGeneMatchings---------'''

class Alpha(object):
	def __init__(self, first, second, name):
		self.lista1 = first
		self.lista2 = second
		self.name = name

def getFmly(genoma):
	fmly = {}
	# create dictionary {gene family : positions of family in genome}
	for idx, itm in enumerate(genoma):
	    if(itm not in fmly):
	        fmly[itm] = [idx]
	    else:
	        fmly[itm].extend([idx])

	return fmly

def getcm(alpha):
	return cm(alpha.lista1, alpha.lista2)

#a segunda maneira (modeTwo) de se encontrar eh de maneira recursiva
def modeTwo():
	allMatches = []
	matchList = ['' for i in alphaList]
	startTime = time.time()	
	return getAllMatches(allMatches, matchList, 0), time.time() - startTime

def findAllMatchings(pathToInput):
	print ('to aqui')
	#sys.argv: [..., pathToInput, 'keyword']
	inputFile = open(pathToInput, "r")
	genoma1, genoma2 = inputFile.readlines()

	fmly1 = getFmly(genoma1.split())
	fmly2 = getFmly(genoma2.split())

	alphaList = [Alpha(fmly1[i], fmly2[i], i) for i in fmly1]
	#print alphaList[0].lista2
	#sequencial
	#modeOne(alphaList, genoma1, genoma2)
	sp.call(['mpiexec', '-np', '300', '-hostfile', 'maquinas', 'modeOne_paralelo.py', pathToInput])
	print ('to aqui')
	#sp.call(['mpiexec', '-np', 'numProcs', '--hostfile', 'maquinas', 'python','modeOne_paralelo.py', 'input1'])