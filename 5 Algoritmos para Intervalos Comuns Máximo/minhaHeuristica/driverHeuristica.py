import sys
sys.path.insert(0, '../minhaHeuristica')	
from ipslon import *
from random import randint
from operations import * 

import time 
import os

# check() verifica se a lista recebida como parametro
# tem elementos repetidos ou nao
def check(lista, nome):
	if len(lista) != len(set(lista)):
		print '%s Tem duplo' % nome
		exit()
	else:
		print '%s Nao tem duplo' % nome

def printUsage():
	print 'Incorrect usage!! Correct usage: driverHeuristica.py <inputFile> <numAttempts>'
	print 'Exiting'
	#exit()

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print sys.argv
		printUsage() #and exit!


	#calculo do tempo de execucao da heuristica
	startTime = time.time()

	pathToInput = os.getcwd().replace('minhaHeuristica', 'genomasDeInput/%s' % sys.argv[1])

	#arquivo com input para execucao
	myFile = open(pathToInput)

	genoma1 = myFile.readline().split()
	genoma2 = myFile.readline().split()
	
	print 'Genomas iniciais:\n%r\n%r\n' % (genoma1, genoma2)

	Y = Ipslon(genoma1, genoma2)
	g1, g2 = Y.spitMatching()

	l1 = [ord(item) for item in g1]
	l2 = [ord(item) for item in g2]

	print '\nApos instanciacao das classes e remocao dos genes imapeaveis: \n%r\n%r\n' % (l1, l2)
	
	# inicio do processo da heuristica
	numCI, listOfCIs = getNumberOfCommonIntervals(g1, g2)

	# lista de strings (matchings) ja analisados
	#compared1 = []
	compared2 = []

	numAttempts = int(sys.argv[2])# Importante p/ complexidade
	for i in range(numAttempts): #Trabalhar nessa numAttempts aqui, eh essencial!

		str1, str2 = Y.disturb()
		#if str1 in compared1 or str2 in compared2: #str1 sempre sera igual aqui!
		if str2 in compared2:
			continue
		else:
			numAux, lstCIs = getNumberOfCommonIntervals(str1, str2)
			if numAux > numCI:
				numCI = numAux
				listOfCIs = lstCIs
				g1, g2 = str1, str2

			compared2.append(str2)

	timeSpent = time.time() - startTime

	# fazQuadro() cria e escreve um arquivo com o mesmo nome da entrada
	# contendo uma visualizacao dos intervalos comuns encontrados no maximum-matching definido 
	# (aleatoriamente) pela heuristica

	#fazQuadro(sys.argv[1], listOfCIs, g1, g2)

	testName = sys.argv[1]

	pathToOutput = os.getcwd().replace('minhaHeuristica', 'saidas/minhaHeuristicaSaidas/mainResultsHeuristica')

	#escreve no arq de saida: testName numAttempts result timeSpent
	outFile = open(pathToOutput, 'a+')
	outFile.write("%s %d %d %f\n" % (testName, numAttempts, numCI, timeSpent)) 

	#numCI armazena o resultado final da heuristica
	print 'numCommonIntervals final: %d' % (numCI)
