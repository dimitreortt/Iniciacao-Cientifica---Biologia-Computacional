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

	listaDeRemovidosdeAux1 = []
	for idx, gene in reversed(list(enumerate(aux1))):
		if gene not in aux2 and gene != 'X':
			aux1.pop(idx)
			listaDeRemovidosdeAux1.append(idx)

	listaDeRemovidosdeAux2 = []
	for idx, gene in reversed(list(enumerate(aux2))):
		if gene not in aux1 and gene != 'Y':
			aux2.pop(idx)
			listaDeRemovidosdeAux1.append(idx)

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

if __name__ == '__main__':

	#------- Inicializa arquivo de entrada -------#
	pathToInput = sys.argv[1]
	inputFile = open(pathToInput, 'r')
	inputName = pathToInput.split('/')[-1]

	#------- leia entradas -------#
	genomeA = inputFile.readline().rstrip('\n').split()
	genomeB = inputFile.readline().rstrip('\n').split()

	#------- driver IILCS -------#
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

		#removeUnmatchable is the key difference between ILCS and IILCS
		aux1, aux2, lisRemoved1, lisRemoved2 = removeUnmatchable(aux1, aux2)
		#print '\ng1: %s\ng2: %s\nmatches: %r\n\n' % (aux1, aux2, matches)
		matchData = lcs(aux1, aux2)
	# recstrings soh recupera os mapeaveis, logo, exclui imapeaveis
	genomeA, genomeB = recStrings(gatherMatches) #-> imprime na saida: 

	genomeA = [str(ord(item)) for item in genomeA]
	genomeB = [str(ord(item)) for item in genomeB]

	totalTimeIILCS = time.time() - startTime

	outFile = open('IILCS/%s_IILCS' % inputName, 'w')
	outFile.write('%s\n%s\n' % (' '.join(genomeA), ' '.join(genomeB)))
	outFile.write('time spent in IILCS: %f' % totalTimeIILCS)
	#-------------------------------#
	outFile.close()

	newpathToInput = os.getcwd()+'/IILCS/%s_IILCS' % inputName
	newpathToOutput = os.getcwd().replace('3heuristicas', 'saidas/3heuristicasSaidas/IILCS/%s_IILCS' % inputName)
	
	#---- Roda Gurobi com a Saida ----#

	os.chdir(os.getcwd().replace('3heuristicas', 'gurobi'))
	subprocess.call(shlex.split('gurobi.sh maxCI.py %s 1 2 3 isHeu %s' % (newpathToInput, newpathToOutput)))