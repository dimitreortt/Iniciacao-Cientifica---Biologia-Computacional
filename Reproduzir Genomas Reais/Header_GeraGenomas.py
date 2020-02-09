from math import ceil
import random

class variable():

	def __init__(self, name, lb, ub):
		self.lowerBound = lb
		self.upperdBound = ub
		self.name = name

		self.currentShot = 0
		self.factor = 0
		self.range = self.upperdBound - self.lowerBound

	def __str__(self):
		return "(%d < %s < %d)" % (self.lowerBound, self.name, self.upperdBound)

	def firstShot(self):
		self.currentShot = (self.lowerBound + self.upperdBound) / 2

	def setFactor(self, factor):
		self.factor = factor

	def printCurrentShot(self):
		print "%s's currentShot is: %d --- " % (self.name ,self.currentShot), self	

	def printFactor(self):
		print "%s's factor is: %d --- " % (self.name ,self.factor), self	

def printv(varlist):
	for var in varlist:
		print var

def firstShot(varlist):
	for var in varlist:
		var.firstShot()

def currentShot(varlist):
	for var in varlist:
		var.printCurrentShot()

def factors(varlist):
	for var in varlist:
		var.printFactor()

def updateCurrentshot(varlist, difference):
	for var in varlist:
		var.currentShot += ceil((difference*var.range)/100.0)
		if var.currentShot < var.lowerBound:
			var.currentShot += 5
		#print ceil((difference*var.range)/100.0), difference, var.range, difference*var.range, ceil(-0.5), ceil(0.5), (difference*var.range)/100.0

	print "Updated Correctly!! Difference was: %d" % (difference)

def somatory(varlist):
	soma = 0
	for var in varlist:
		soma += var.currentShot*var.factor
	print "current sum is: %s, goal sum is 26148" % soma
	return soma
#somatory.goalsum = 26148

def addCoordinates(varlist, coordinates):
	for c in coordinates:
		varName, factor = c.split('*')
		for v in varlist:
			if v.name == varName:
				v.setFactor(int(factor))
				break

def findSolutionForLinearSystem():
	sysfile = open("sistemaLinear")
	
	linearSystem = sysfile.readline()

	coordinates = [item for item in linearSystem.split(' + ') if '*' in item]
	print coordinates	

	while "Subject to:" not in sysfile.readline():
		pass

	variables = []
	for line in sysfile.readlines():
		elements = line.split()
		
		lb, junk1, name, junk2, ub = elements
		variables.append(variable(name, int(lb), int(ub)))

	firstShot(variables)
	currentShot(variables)
	addCoordinates(variables, coordinates)
	#factors(variables)

	somatory(variables)
	change = input("What is next shot?")
	while change != 0:		
		updateCurrentshot(variables, change)
		somatory(variables)
		change = input("What is next shot?")

	currentShot(variables)

def createGeneBank(families):
	allGenes = []
	for f in families:
		allGenes.extend(f.genes)

	return allGenes

def startSize13(families, genomes):
	random.shuffle(families)
	count = 0
	for idx,f in enumerate(families):
		if count < 200:
			if f.size >= 13:
				for g in genomes:
					g.insertGene(f.genes.pop(0))
					#print len(f.genomesPresence), count
					#print f.genes, len(f.genes)
				f.size -= 13
				count += 1
				#print len(f.genomesPresence), count
	#exit()

def startSize12(families, genomes):
	random.shuffle(families)
	random.shuffle(genomes)
	count = 0
	for idx,f in enumerate(families):
		if count < 200:
			if f.size >= 12:
				for g in genomes[:-1]:
					g.insertGene(f.genes.pop(0))
					#print len(f.genomesPresence), count
					#print f.genes, len(f.genes)
				f.size -= 12
				count += 1
				#print len(f.genomesPresence), count
	#exit()

def startSize11(families, genomes):
	random.shuffle(families)
	random.shuffle(genomes)
	count = 0
	for idx,f in enumerate(families):
		if count < 130:
			if f.size >= 11:
				for g in genomes[:-2]:
					g.insertGene(f.genes.pop(0))
					#print len(f.genomesPresence), count
					#print f.genes, len(f.genes)
				f.size -= 11
				count += 1
				#print len(f.genomesPresence), count
	#exit()

def startSize10(families, genomes):
	random.shuffle(families)
	random.shuffle(genomes)
	count = 0
	for idx,f in enumerate(families):
		if count < 50:
			if f.size >= 10:
				for g in genomes[:-3]:
					g.insertGene(f.genes.pop(0))
					#print len(f.genomesPresence), count
					#print f.genes, len(f.genes)
				f.size -= 10
				count += 1
				#print len(f.genomesPresence), count
	#exit()

def startSize9(families, genomes):
	random.shuffle(families)
	random.shuffle(genomes)
	count = 0
	for idx,f in enumerate(families):
		if count < 200:
			if f.size >= 9:
				for g in genomes[:-4]:
					g.insertGene(f.genes.pop(0))
					#print len(f.genomesPresence), count
					#print f.genes, len(f.genes)
				f.size -= 9
				count += 1
				#print len(f.genomesPresence), count
	#exit()

def atributeOrphans(families, genomes):
	random.shuffle(families)
	for g in genomes:
		count = 0
		inserted = ''
		while count < g.numberOfOrphans:
			for f in families:
				if f.size == 1:
					newGene = f.genes.pop(0)
					inserted += "%d " % newGene.value
					g.insertGene(newGene)
					count += 1
					f.size -= 1
					break
					
		print "%s recebeu %d orphans: %s" % (g.name, count, inserted)


def saveOutput(families, genomes):
	fs = familiesPerSpecies = {}
	for f in families:
		l = len(f.genomesPresence) 
		if l not in fs:
			fs[l] = 1
		else:
			fs[l] += 1

	#print fs
	output = open("familiesPerSpecies", 'w')
	for i, value in fs.items():
		print i, value
		output.write("%r %r\n" % (i,value))

	for g in genomes:
		gfile = open(g.name, 'w')

		random.shuffle(g.genes)

		sequencia = ''
		for gene in g.genes:
			sequencia += '%d ' % (gene.value)

		gfile.write(sequencia)

		gfile.close()


