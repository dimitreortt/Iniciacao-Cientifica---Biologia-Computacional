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

if __name__ == '__main__':
	#------- Inicializa arquivo de entrada -------#
	pathToInput = sys.argv[1]
	inputFile = open(pathToInput, 'r')
	inputName = pathToInput.split('/')[-1]

	#------- leia entradas -------#
	genomeA = inputFile.readline().rstrip('\n').split()
	genomeB = inputFile.readline().rstrip('\n').split()

	#------- Processo - ILCS -------#
	startTime = time.time()
	gatherMatches = []

	#lcs stands for longest common substring
	matchData = lcs(genomeA, genomeB)
	
	auxGenome1, auxGenome2 = genomeA, genomeB
	while(matchData):

		auxGenome1, auxGenome2, matches = mark(auxGenome1, auxGenome2, matchData)
		#print '\ng1: %s\ng2: %s\nmatches: %r\n\n' % (auxGenome1, auxGenome2, matches)
		gatherMatches.extend(matches)
		matchData = lcs(auxGenome1, auxGenome2)
	
	# recstrings retorna uma lista de chrs unicos
	# recstrings soh recupera os mapeaveis, logo, exclui imapeaveis
	genomeA, genomeB = recStrings(gatherMatches) #-> imprime na saida: 

	genomeA = [str(ord(item)) for item in genomeA]
	genomeB = [str(ord(item)) for item in genomeB]

	totalTimeILCS = time.time() - startTime

	outFile = open('ILCS/%s_ILCS' % inputName, 'w')
	outFile.write('%s\n%s\n' % (' '.join(genomeA), ' '.join(genomeB)))
	outFile.write('time spent in ILCS: %f' % totalTimeILCS)
	#-------------------------------#
	outFile.close()

	newpathToInput = os.getcwd()+'/ILCS/%s_ILCS' % inputName
	newpathToOutput = os.getcwd().replace('3heuristicas', 'saidas/3heuristicasSaidas/ILCS/%s_ILCS' % inputName)
	
	#---- Roda Gurobi com a Saida ----#

	os.chdir(os.getcwd().replace('3heuristicas', 'gurobi'))
	subprocess.call(shlex.split('gurobi.sh maxCI.py %s 1 2 3 isHeu %s' % (newpathToInput, newpathToOutput)))
