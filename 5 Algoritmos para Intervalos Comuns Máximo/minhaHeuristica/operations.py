from random import randint
from collections import Counter
import copy

def sameContent(inp, ent):
   if Counter(inp) == Counter(ent): 
      return True
   else: 
      return False

def getNumberOfCommonIntervals(string1, string2):
	len1 = len(string1)
	len2 = len(string2)

	list1 = [(a,b) for a in range(len1) for b in range(a, len1)]
	list2 = [(a,b) for a in range(len2) for b in range(a, len2)]

	listOfCIs = []
	numberOfCommonIntervals = 0

	# para cada substring em string1, pesquise pela ocorrencia
	# da mesma na string2
	for tupla in list1:
		# start = comeco da substring, end = fim da substring
		start, end = tupla
		firstSubstring = string1[start:end+1]

	  	for other in list2:
	  		# start = comeco da substring, end = fim da substring
	  		start, end = other
		  	secondSubstring = string2[start:end+1]

		  	# se ambas as substrings possuem o mesmo conteudo,
		  	# entao conte como um Intervalo Comum!
			if sameContent(firstSubstring, secondSubstring):
				listOfCIs.append([tupla, other])
				numberOfCommonIntervals += 1
				break

	return numberOfCommonIntervals, listOfCIs

def getMainList(leftList, rightList):
	return list(set(leftList) - set(rightList))

def getTupleList(listaA, listaB):
	
	listaBufferA = []
	listaBufferB = []

	menor = min(len(listaA), len(listaB))
	# inicilizando a lista de tuplas
	tupleList = ['' for i in range(menor)]

	# defina a lista de tuplas aleatoriamente:
	for i in range(menor):
		# mainList contem a lista de genes ainda nao mapeados ("disponiveis")
		# da familia de genes
		mainListA = getMainList(listaA, listaBufferA)
		mainListB = getMainList(listaB, listaBufferB)

		a = mainListA[randint(0,len(mainListA) - 1)]
		listaBufferA.append(a)

		b = mainListB[randint(0,len(mainListB) - 1)]
		listaBufferB.append(b)
		
		tupleList[i] = [a,b,a]
		
	return tupleList

# prduz uma saida para analise em um arquivo extra
def produzLinha(lcdt, l1, l2):
# lcdt - lista com duas tuplas

	g1 = [str(ord(item)) for item in l1]
	g2 = [str(ord(item)) for item in l2]

	g1.insert(lcdt[0][0], '[')
	g1.insert(lcdt[0][1]+2, ']')

	g2.insert(lcdt[1][0], '[')
	g2.insert(lcdt[1][1]+2, ']')

	return 'o IC: %r\ng1: %s\ng2: %s\n\n' % (lcdt, ' '.join(g1), ' '.join(g2))

# produz um quadro com todos os intervalos comuns do teste realizado
def fazQuadro(nome, listOfCIs, g1, g2):
	f1 = ' '.join([str(ord(item)) for item in g1])
	f2 = ' '.join([str(ord(item)) for item in g2])

	myFile = open(nome + '_quadro_heu', 'w')
	a = f1 + '\n' + f2 + '\n\n'
	myFile.write(a)
	for i in listOfCIs:
		myFile.write(produzLinha(i, g1, g2))

# remove da lista as posicoes estrategicamente vazias
def fixRange(lista):
	for idx, i in reversed(list(enumerate(lista))):
		if i == '':
			lista.pop(idx)
	return lista
