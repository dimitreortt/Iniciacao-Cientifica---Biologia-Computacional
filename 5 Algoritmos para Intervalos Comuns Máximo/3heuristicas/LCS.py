from difflib import SequenceMatcher 

def matchsubstring(m,n): 
   #print 'mn', m,n
   if type(m) != type([]) or type(n) != type([]):
   	  print 'Finish all executions!! Dealing with strings instead of Types! Exiting...'
   	  exit()
   seqMatch = SequenceMatcher(None,m,n) 
   match = seqMatch.find_longest_match(0, len(m), 0, len(n)) 
   '''if (match.size!=0): 
      print ("Common Substring ::>",m[match.a: match.a + match.size])
   else: 
      print ('No longest common sub-string found') '''

   return match
   #return m[match.a: match.a + match.size]

def rev(string):
	return [item for item in reversed(string)]

def lcs(str1, str2):
	rght = matchsubstring(str1, str2)
	left = matchsubstring(str1, rev(str2))

	#buildMatchData:#
	matchData = ['','']
	if rght.size == 0 and left.size == 0:
		return None

	elif rght.size > left.size:
		match = rght
		first = [i for i in range(match.a, match.a + match.size)]
		secnd = [i for i in range(match.b, match.b + match.size)]
	else:
		match = left
		first = [i for i in range(match.a, match.a + match.size)]
		secnd = [i for i in range(match.b, match.b + match.size)]
		secnd = [len(str2) - i - 1 for i in secnd]

	matchData = [first, secnd]
	#print matchData
	return matchData

def mark(g1,g2,matchData):
	fst, sec = matchData

	listOfMatchings = [[fst[i], sec[i], fst[i]] for i in range(len(fst))]

	lisg1 = list(g1)
	lisg2 = list(g2)

	for i in fst:
		lisg1[i] = "X"

	for i in sec:
		lisg2[i] = "Y"

	#g1, g2 = ''.join(lisg1), ''.join(lisg2)
	g1, g2 = lisg1, lisg2

	return g1, g2, listOfMatchings

# remove da lista as posicoes estrategicamente vazias
def fixRange(lista):
	for idx, i in reversed(list(enumerate(lista))):
		if i == '':
			lista.pop(idx)
	return lista

def getStrings(listOfMatchings):
	#a = max(len(self.genoma1), len(self.genoma2))
	a = 100 # mais facil
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

if __name__ == '__main__':

	#g1,g2 = le strings
	g1, g2 = 'amoraisdjaoisjdjksdoaisjdaklsddesione', 'romaenoiseddsaskdnlasndmlaskdmnalksnd'
	
	gatherMatches = []
	matchData = lcs(g1, g2)
	#print matchData
	while(matchData):
		g1aux, g2aux, matches = mark(g1, g2, matchData)
		
		gatherMatches.extend(matches)
		matchData = lcs(g1aux, g2aux)	

	#print gatherMatches

	#matches = removeUnmatched(gatherMatches)

	#recStrings(gatherMatches) -> imprime na saida: 
	#lcs('amoraisdjaoisjdjksdoaisjdaklsddesione', 'romaenoiseddsaskdnlasndmlaskdmnalksnd')

