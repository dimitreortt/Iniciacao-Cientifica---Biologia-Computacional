# essa eh a classe principal da heuristica, que manipula os calculos com os genomas
# quaisquer calculos de estatisticas devem ser implementadas aqui
from alpha import Alpha
from operations import fixRange
import copy

def getFmly(genoma):
	fmly = {}
	# create dictionary {gene family : positions of family in genome}
	for idx, itm in enumerate(genoma):
	    if(itm not in fmly):
	        fmly[itm] = [idx]
	    else:
	        fmly[itm].extend([idx])

	return fmly

def fixGenomes(lista1, lista2):
	for i in reversed(lista1):
		if i not in lista2:
			lista1.remove(i)

	for i in reversed(lista2):
		if i not in lista1:
			lista2.remove(i)	

class Ipslon(object):
	# listaDeFamilias = [Alphas]

	def __init__(self, str1, str2):

		str1, str2 = list(str1), list(str2)
		
		fixGenomes(str1, str2) #fixGenomes remove genes imapeaveis
		
		print 'Genomas apos remocao de genes imapeaveis: \n%r\n%r' % (str1, str2)

		self.genoma1 = str1
		self.genoma2 = str2

		fmly1 = getFmly(self.genoma1)
		fmly2 = getFmly(self.genoma2)

		# listaDeFamilias = [alpha(posG1, posG2, geneId) para 'gene' em 'Genoma']
		self.listaDeFamilias = [Alpha(fmly1[i], fmly2[i], i) for i in fmly1]

	def disturb(self): 
		for alpha in self.listaDeFamilias:
			alpha.disturb()

		return self.recoverStrings()

	def spitMatching(self):
		for alpha in self.listaDeFamilias:
			alpha.start(self)

		return self.recoverStrings()
		
	def recoverStrings(self):
		firstString = ''
		secondString = ''

		# recebe todos os mapeamentos atuais
		listOfMatchings = self.getMatchings()

		# cpy1 e cpy2 recebem as strings correspondentes ao matching realizado, com os genes
		# que nao sao mapeados sendo removidos	
		cpy1, cpy2 = self.getStrings(listOfMatchings)
		
		# chrList recebe a lista com os nomes dos genomas traduzida para uma lista
		# com identificadores unicos, atraves do metodo unichr()
		chrList1 = [unichr(int(item)) for item in cpy1]
		chrList2 = [unichr(int(item)) for item in cpy2]

		return ''.join(chrList1), ''.join(chrList2)		

	# este metodo recupera as strings a partir dos matchings atribuidos aleatoriamente	
	def getMatchings(self):
		gatherTupleList = []
		for i in self.listaDeFamilias:
			gatherTupleList.extend(i.getMatchings())

		return gatherTupleList

	def getStrings(self, listOfMatchings):

		a = max(len(self.genoma1), len(self.genoma2))
		
		# inicializa listas para a recuperacao das strings correspondentes
		# aos genomas
		cpy1 = ['' for i in range(a)]
		cpy2 = ['' for i in range(a)]

		# para cada mapeamento faca:
		for i in listOfMatchings:
			# copiaGenoma[pos] = nomeGene
			pos_g1, pos_g2, geneId = i
			cpy1[pos_g1] = geneId
			cpy2[pos_g2] = geneId

		# corrige alcances (posicoes) dos genes apos filtragem 
		# que remove genes imapeaveis - fixRange()
		cpy1 = fixRange(cpy1)
		cpy2 = fixRange(cpy2)

		return cpy1, cpy2	