import time
import copy
import MOops.modeOneIO as io

class Alpha(object):
				def __init__(self, first, second, name):
								self.lista1 = first
								self.lista2 = second
								self.name = name
								self.possib = getcm(self)

				def __str__(self):
					return 'Alpha%s.lista1:%r\nAlpha%s.lista1:%r\nAlpha%s.possib:%r\n' % (self.name, self.lista1, self.name, self.lista2, self.name, self.possib)

def newMatching(match1, match2, match3, match4):
				#print match1, match2, match3, match4
				return [match1, match2, match3, match4]
				#exit()

'''ADICIONAR LISTAS DE MATCHIGNS_INTRA_FAMILIAS POSSIVEIS COM UM EXTEND SEILA
DISTRIBUIR ESSAS LISTAS DE matchings
cada processador pega uma lista e calcula todas possibilidades
a partir desta lista
(nao vejo tanta dificuldade nisso, n sei pq ta empacado)
(descobrir pq ta empacado e fazer passo a passo
com passos mais simples possiveis)'''

def getFmly(genoma):
				fmly = {}
				# create dictionary {gene family : positions of family in genome}
				for idx, itm in enumerate(genoma):
								if(itm not in fmly):
												fmly[itm] = [idx]
								else:
												fmly[itm].extend([idx])

				return fmly

def newAlphaList(pathToInput):
				#pathToInput = 'input0'
				#sys.argv: [..., pathToInput, 'keyword']
				print (pathToInput+'nai', 'asdasd')
				inputFile = open(pathToInput, "r")
				genoma1, genoma2 = inputFile.readlines()
				#print('to aqui')
				#exit()
				fmly1 = getFmly(genoma1.split())
				fmly2 = getFmly(genoma2.split())

				alphaList = [Alpha(fmly1[i], fmly2[i], i) for i in fmly1]
				return alphaList, genoma1, genoma2 

# Essa funcao retorna uma lista de tamanho 6(no topo da recursao claro...)
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
				#print listaAll, 'a'

				return listaAll

def getcm(alpha):
				#print alpha.lista1, alpha.lista2
				#print collectAllGeneMatchings(alpha.lista1, alpha.lista2), 'i am exiting for test purposes'
				return collectAllGeneMatchings(alpha.lista1, alpha.lista2)

def organize(lista, size):
				newFirsts = []

				smallerPortion =  len(lista)/size
				biggerPortion = smallerPortion+1
				#number of bigger portions, used to get the items that were left behind
				#in first implementation
				numOfBiggers = len(lista)%size
				numOfSmallers = size-numOfBiggers

				for i in range(numOfBiggers):
					currentPortion = lista[i*biggerPortion:(i+1)*biggerPortion]
					newFirsts.append(currentPortion)

				start = numOfBiggers*biggerPortion
				for i in range(numOfSmallers):
					currentPortion = lista[start+i*smallerPortion : start+(i+1)*smallerPortion]
					newFirsts.append(currentPortion)

				print 'len de newFirsts eh: %d' % len(newFirsts)
				#for item in newFirsts:
				#	assert len(item) == 6
				print ('asserted fine')
				return newFirsts

def getFmly(genoma):
	fmly = {}
	# create dictionary {gene family : positions of family in genome}
	for idx, itm in enumerate(genoma):
		if(itm not in fmly):
			fmly[itm] = [idx]
		else:
			fmly[itm].extend([idx])

	return fmly


def gatherLosangos(finalResults):
	dic = {}
	for result in finalResults:
		for item in result.globalResults:
			if item in dic:
				dic[item] += result.globalResults[item]
			else:
				dic[item] = result.globalResults[item]

	return dic
