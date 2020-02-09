from random import randint
from collections import Counter
import copy

#dadas duas listas de posicoes, como eu encontro todos os geneMatchings possiveis

def collectAllGeneMatchings(lista1, lista2):

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