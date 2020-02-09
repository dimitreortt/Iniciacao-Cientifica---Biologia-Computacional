import MOops.modeOneStrings as st
from MOops.getNumCIs import getNumberOfCommonIntervals as nCIs

#def getLocalResults(listOfMM, genoma1, genoma2):
def getLocalResults(listOfMM):
	#assert len(listOfMM[0]) == 10
	#assert len(listOfMM) == 6
	#print 'lsosos', listOfMM
	# para cada Maximum Matching na lista de Todos os Maximum Matchings
	# existentes para esse genoma faca:
	localResults = []
	for MM in listOfMM:
		#print MM, len(MM)
		#exit()
		strG1, strG2 = st.recoverStrings(MM)
		numCIs, listOfCIs = nCIs(strG1, strG2)
		#print st.getStrings(MM)
		localResults.append((numCIs, listOfCIs))
		#print localResults
		#print '\n\n\n#--------------------------------------#'
	return localResults

