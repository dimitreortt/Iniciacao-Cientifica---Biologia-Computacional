# a classe alpha representa uma familia de genes e tem duas listas contendo as presencas
# dessa familia no genoma1 e no genoma2

#------------ libraries ------------#
from geneMatching import GeneMatching
from operations import getTupleList
from random import randint

#------------ matters --------------#
class Alpha(object):

	def __init__(self, first, second, name):
		self.lista1 = first
		self.lista2 = second
		self.name = name

	#este metodo faz a atribuicao do primeiro geneMatching (aleatoriamente) e atribui a self.currentMathcing
	def start(self, Y):
		# self.used e uma lista para calculos locais, 
		# ela armazena os conjuntos de matchings ja utilizados
		self.used = [] 
		tupleList = getTupleList(self.lista1, self.lista2)
		self.currentMatching = GeneMatching(tupleList)
		self.used.append(self.currentMatching)

	def getMatchings(self):
		return self.currentMatching.tupleList

	def disturb(self):
		# Importante para a complexidade
		a = randint(1, min(len(self.lista1), (self.lista2)))
		#a = randint(1,2)
		for i in range(a): ###### ALTERAR ESSE FOR, INFLUENCIA MUITO A COMPLEXIDADE!!
			#tabalhar o parametro do range: talvez dividi-lo por 2...
			
			tupleList = getTupleList(self.lista1, self.lista2)
			buf = GeneMatching(tupleList)
			if buf.notIn(self.used):
				self.currentMatching = buf
				self.used.append(buf)
				break
