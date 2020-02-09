import sys
tamanho = int(sys.argv[1])

folderName = sys.argv[0].split('/')[-2]

outputFile = open(folderName+'/modeOne.py', 'w')
outputFile.write('import time\n')
outputFile.write('from collectGeneMatchings import collectAllGeneMatchings as cm\n\n')
outputFile.write('def getcm(alpha):\n')
outputFile.write('\treturn cm(alpha.lista1, alpha.lista2)\n\n')
outputFile.write('def modeOne(alphaList):\n')
outputFile.write('\tstartTime = time.time()\n\n')

alphas = ', '.join(['alpha%d' % i for i in range(1, tamanho+1)])

outputFile.write('\t%s = alphaList\n' % alphas)
outputFile.write('\tallMatches = []\n')

for i in range(tamanho):
	outputFile.write('%sfor match%d in getcm(alpha%d):\n' % ((i+1)*'\t'	,i+1, i+1))

matches = ', '.join(['match%d' % i for i in range(1, tamanho+1)])

outputFile.write('%sallMatches.append([%s])\n\n' % ((tamanho+1)*'\t', matches))

getcms = ' '.join(['for match%d in getcm(alpha%d)' % (i,i) for i in range(1, tamanho+1)])

outputFile.write('\tallMatches = [[%s] %s]\n' % (matches, getcms))
outputFile.write('\treturn allMatches, time.time() - startTime')

'''
def modeOne():
	startTime = time.time()

	alpha1, alpha2, alpha3, alpha4 = alphaList	
	allMatches = []
	for match1 in getcm(alpha1):
		for match2 in getcm(alpha2):
			for match3 in getcm(alpha3):
				for match4 in getcm(alpha4):
					allMatches.append([match1, match2, match3, match4])

	allMatches = [[match1, match2, match3, match4] for match1 in getcm(alpha1) for match2 in getcm(alpha2) for match3 in getcm(alpha3) for match4 in getcm(alpha4)]
	return allMatches, time.time() - startTime'''
