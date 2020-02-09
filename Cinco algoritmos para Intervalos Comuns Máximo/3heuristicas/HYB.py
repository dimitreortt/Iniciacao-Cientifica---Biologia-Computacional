import sys
sys.path.insert(0, '../3heuristicas')
from LCS import lcs
from LCS import mark
from LCS import getStrings
import time
#from LCS import getStrings

def recStrings(listOfMatchings):
	cpy1 = ['' for i in range(100)] #100 pois eh mais facil
	cpy2 = ['' for i in range(100)]

	for i in listOfMatchings:
		pos_g1, pos_g2, geneId = i
		cpy1[pos_g1] = geneId
		cpy2[pos_g2] = geneId

	#fixrange(cpy1)
	for idx, i in reversed(list(enumerate(cpy1))):
		if i == '':
			cpy1.pop(idx)

	#fixrange(cpy2)
	for idx, i in reversed(list(enumerate(cpy2))):
		if i == '':
			cpy2.pop(idx)
	
	chrList1 = [unichr(int(item)) for item in cpy1]
	chrList2 = [unichr(int(item)) for item in cpy2]

	return ''.join(chrList1), ''.join(chrList2)

def removeUnmatchable(aux1, aux2):
	aux1 = list(aux1) #ja chega sendo lista
	aux2 = list(aux2)
	#print 'to em removeUnmatchable'

	listaDeRemovidosdeAux1 = []
	for idx, gene in reversed(list(enumerate(aux1))):
		if gene not in aux2 and gene != 'X':
			#print 'deletando g1[%d]' % idx
			aux1.pop(idx)
			listaDeRemovidosdeAux1.append(idx)

	listaDeRemovidosdeAux2 = []
	for idx, gene in reversed(list(enumerate(aux2))):
		if gene not in aux1 and gene != 'Y':
			#print 'deletando g2[%d]' % idx
			aux2.pop(idx)
			listaDeRemovidosdeAux1.append(idx)

	#print 'lr1: %r\nlr2: %r' % (listaDeRemovidosdeAux1, listaDeRemovidosdeAux2)
	return aux1, aux2, listaDeRemovidosdeAux1, listaDeRemovidosdeAux2

def fixMatches(matches, l1, l2):
	for match in matches:

		for i in l1:
			if i <= match[0]:
				match[0] += 1

		for i in l2:
			if i <= match[1]:
				match[1] += 1

		#match = check(match, l1, l2)
	return matches

def HYB_Condition(matchData):
	#matchData -> [[firstList], [secList]]
	if len(matchData[0]) < 2:
		return False
	else:
		return True

def getSaved(l1, l2):
	saved = {}
	for idx, i in enumerate(l1):
		if i != 'X':
			if i not in saved:
				saved[i] = [[idx],[]]
			else:
				saved[i][0].append(idx)

	for idx, i in enumerate(l2): 
		if i != 'Y':
			if i not in saved:
				saved[i] = [[],[idx]]
			else:
				saved[i][1].append(idx)

	return saved

def insertSaved(g1, g2, saved):
	
	queue1 = []
	queue2 = []
	count = 1
	for gene in saved:

		gname = str(max([int(str(i)) for i in g1])+count)
		count += 1
		# saved: {'gname' : [[lis1],[lis2]]}
		lis1, lis2 = saved[gene]

		queue1.extend([(item,gname) for item in lis1])
		queue2.extend([(item,gname) for item in lis2])

 	queue1.sort(key=lambda tup: tup[0])
 	queue2.sort(key=lambda tup: tup[0])
 	
 	for gene in queue1:
 		pos, geneName = gene
		g1.insert(pos, geneName)

	for gene in queue2:
 		pos, geneName = gene
		g2.insert(pos, geneName)

	return g1, g2

if __name__ == '__main__':

	#------- Inicializa arquivo de entrada -------#
	pathToInput = sys.argv[1]
	inputFile = open(pathToInput, 'r')
	inputName = pathToInput.split('/')[-1]

	#------- leia entradas -------#
	genomeA = inputFile.readline().rstrip('\n').split()
	genomeB = inputFile.readline().rstrip('\n').split()

	#------- driver HYB -------#
	startTime = time.time()
	gatherMatches = []

	#lcs stands for longest common substring
	matchData = lcs(genomeA, genomeB)
	
	aux1, aux2 = genomeA, genomeB
	lisRemoved1, lisRemoved2 = [], []
	while(matchData):		
		aux1, aux2, matches = mark(aux1, aux2, matchData)
		matches = fixMatches(matches, lisRemoved1, lisRemoved2)
		gatherMatches.extend(matches)

		#removeUnmatchable is the key difference between ILCS and HYB
		aux1, aux2, lisRemoved1, lisRemoved2 = removeUnmatchable(aux1, aux2)
		#print '\ng1: %s\ng2: %s\nmatches: %r\n\n' % (aux1, aux2, matches)
		
		matchData = lcs(aux1, aux2)
		if not HYB_Condition(matchData):
			print 'Entrei no hyb_condition'
			break

	#print aux1, aux2
	saved = getSaved(aux1, aux2)

	#print saved
	
	# recstrings soh recupera os mapeaveis, logo, exclui imapeaveis
	genomeA, genomeB = recStrings(gatherMatches) #-> imprime na saida: 

	genomeA = [str(ord(item)) for item in genomeA]
	genomeB = [str(ord(item)) for item in genomeB]
	
	genomeA, genomeB = insertSaved(genomeA, genomeB, saved)
	
	totalTimeHYB = time.time() - startTime

	outFile = open('HYB/%s_HYB' % inputName, 'w')
	outFile.write('%s\n%s\n' % (' '.join(genomeA), ' '.join(genomeB)))
	outFile.write('time spent in HYB: %f' % totalTimeHYB)
	#-------------------------------#
	outFile.close()

	newpathToInput = os.getcwd()+'/HYB/%s_HYB' % inputName
	newpathToOutput = os.getcwd().replace('3heuristicas', 'saidas/3heuristicasSaidas/HYB/%s_HYB' % inputName)
	
	#---- Roda Gurobi com a Saida ----#

	os.chdir(os.getcwd().replace('3heuristicas', 'gurobi'))
	subprocess.call(shlex.split('gurobi.sh maxCI.py %s 1 2 3 isHeu %s' % (newpathToInput, newpathToOutput)))