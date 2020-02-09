def func(it):
	return [item for item in it]

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