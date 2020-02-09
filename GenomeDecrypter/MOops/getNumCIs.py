from time import time
from collections import Counter

def getNumberOfCommonIntervals(string1, string2):
	len1 = len(string1)
	len2 = len(string2)
	#assert len1 == 30 & len2 == 30
	startTime = time()

	#list1 = [(a,b) for a in range(len1) for b in range(a, len1)]
	#list2 = [(a,b) for a in range(len2) for b in range(a, len2)]

	list1, list2 = getNumberOfCommonIntervals.lista1, getNumberOfCommonIntervals.lista2

	listOfCIs = []
	numberOfCommonIntervals = 0
	count = 0
	# para cada substring em string1, pesquise pela ocorrencia
	# da mesma na string2
	for tupla in list1:
		# start = comeco da substring, end = fim da substring
		start, end = tupla
		firstSubstring = string1[start:end+1]
		
		len1 = len(firstSubstring)

		if len1 == 1:
			if firstSubstring in string2:
				numberOfCommonIntervals += 1
				listOfCIs.append(tupla)
				#count += 1
				#print count
			continue

		if len1 == 2:
			if firstSubstring in string2 or firstSubstring[1]+firstSubstring[0] in string2:
				numberOfCommonIntervals += 1
				listOfCIs.append(tupla)
				#count += 1
				#print count
			continue

		for other in list2:
			# start = comeco da substring, end = fim da substring
			start, end = other
			# if len2 == len1 ... else: break
			if (end + 1) - start == len1:
				secondSubstring = string2[start:end+1]
				# se ambas as substrings possuem o mesmo conteudo,
				# entao conte como um Intervalo Comum!
				#if sameContent(firstSubstring, secondSubstring):
				if Counter(firstSubstring) == Counter(secondSubstring):
				#if firstSubstring == secondSubstring or firstSubstring == reversed(secondSubstring):
					listOfCIs.append(tupla)
					#listOfCIs.append([tupla, other])
					numberOfCommonIntervals += 1
					break

	if numberOfCommonIntervals <= 23:
		#string1 = [ord(item) for item in string1]
		#string2 = [ord(item) for item in string2]
		#print 'Num invalido, strings:\n%r\n%r\nAbortando...' % (string1, string2)
		#exit()
		pass
	timeInside = time()-startTime
	#print 'Tempo dentro: %f\n' % (timeInside)
	#print 'Tempo fora  : %f' % (startTime - getNumberOfCommonIntervals.time)
	#updateMedia(timeInside)
	#getNumberOfCommonIntervals.time = time()
	#print numberOfCommonIntervals, listOfCIs
	#exit()
	return numberOfCommonIntervals, listOfCIs
getNumberOfCommonIntervals.time = time()
getNumberOfCommonIntervals.lista1 = [(a,b) for a in range(27) for b in range(a, 27)]
getNumberOfCommonIntervals.lista2 = [(a,b) for a in range(27) for b in range(a, 27)]
getNumberOfCommonIntervals.struc = [0.0, 0]

#getNumberOfCommonIntervals.lista = [(a,b) for a in range(30) for b in range(a, 30)]
