from copy import deepcopy
# GeneMatching eh um matching que satisfaca os casamentos de uma familia de genes em um genoma
class GeneMatching():
	def __init__(self, tupleList):
		self.tupleList = deepcopy(tupleList)

	def __eq__(self, other):
		if self.__class__ == other.__class__:
			for i in self.tupleList:
				if i not in other.tupleList:
					return False
			return True
		
		return False

	def notIn(self, lista): # lista[geneMatchings]
		for i in lista:
			if self == i:
				return False

		return True