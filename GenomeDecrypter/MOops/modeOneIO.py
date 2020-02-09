def getGlobalFmly(lst):
	gFmly = {}
	for item in lst:
		a, b = item[0], item[1]
		gFmly[int(a)] = int(b)

	return gFmly

#esse metodo escreve a saida em arquivos auxiliares.
#escrever metodo analogo que escreva a saida somente em variaveis locais,
#dicionarios.
def updateGlobalResults(pathToOutput, localFmly, outFileLines):

	globalFmly = getGlobalFmly(outFileLines)
	for item in localFmly:
		qtd = len(localFmly[item])

		name = item
		if name in globalFmly:
			globalFmly[name] += qtd
		else:			
			globalFmly[name] = qtd

		#outFile = open(pathToOutput, 'w')

	for i in globalFmly:
		qtdPresences = globalFmly[i]
		#outFile.write("%d\t%d\n" % (i, qtdPresences))