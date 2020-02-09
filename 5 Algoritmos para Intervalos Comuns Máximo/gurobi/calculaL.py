def occ(gene, genome, lista):
	count = 0
	for g in genome:
		if g == gene:
			count = count + 1
	return count

def calculaL(GA, GB):
	L = 0
	lista = []
	for g in GA:
		if g not in lista:
			lista.append(g)
			occ1 = occ(g, GA, lista)
			occ2 = occ(g, GB, lista)
			L = L + min(occ1, occ2)

	return L