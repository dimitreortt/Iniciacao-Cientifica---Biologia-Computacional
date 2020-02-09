class familia():
	"""docstring for familia"""
	def __init__(self, size, value):
		self.size = size
		self.value= value
		self.genomesPresence = []
		self.genes = [gene(self, self.value) for i in range(self.size)]
		
	def insertPresence(self,genome):
		if genome not in self.genomesPresence:
			self.genomesPresence.append(genome)
	#def genes(self):
		#return self.genes

class gene():
	def __init__(self, parent, value):
		self.parent = parent
		self.value = value


def createFamilies():
	numero_genes = [7763,2797,1031,610,313,231,232,163,128,101,132,133,220,41,21,14,12,13,13,18,4,14,14,18,
		18,19,12,11,1,1,6,1,1,1,5,1,5,1,6,5,5,6,5,1,1,1,1,1,1,1,1,1,1,1,1]

	sizes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32, 34, 35, 36, 39, 
		41, 43, 44, 45, 46, 49, 50, 52, 54, 56, 57, 59, 63, 65, 70, 100, 128, 404, 544]

	print sum(numero_genes)
	
	soma = 0
	for i in range(55):
		soma+= numero_genes[i]*sizes[i]
	print soma
	#exit()
	families = []
	nameCount = 0
	for idx, num in enumerate(numero_genes):
		for i in range(num):
			nameCount += 1
			families.append(familia(sizes[idx], nameCount))

	print len(families)
	#exit()
	return families