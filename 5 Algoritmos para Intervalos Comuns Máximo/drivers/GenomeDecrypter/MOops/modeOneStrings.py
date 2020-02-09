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
	#print listOfMatchings, len(listOfMatchings), 'he'
	#print len(listOfMatchings)
	#exit()
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
	#assert len(gatherList) == 30
	#print 'entrei', gatherList
	# cpy1 e cpy2 recebem as strings correspondentes ao matching realizado, com os genes
	# que nao sao mapeados sendo removidos	
	cpy1, cpy2 = getStrings(gatherList)
	#assert len(cpy2) == 30
	# chrList recebe a lista com os nomes dos genomas traduzida para uma lista
	# com identificadores unicos, atraves do metodo unichr()
	chrList1 = [unichr(int(item)) for item in cpy1]
	chrList2 = [unichr(int(item)) for item in cpy2]
	return ''.join(chrList1), ''.join(chrList2)