from math import ceil
from random import randint

class genome():
	def __init__(self,name,size,orphans):
		self.name = name
		self.size = size
		self.emptySpaces = size
		self.genes = []
		self.numberOfOrphans = orphans

	def insertGene(self, gene):
		self.genes.append(gene)
		self.emptySpaces -= 1
		gene.parent.insertPresence(self)


	def percent(self):
		#print ceil((self.emptySpaces/self.size)*100), self.emptySpaces, self.size
		return int(ceil((self.emptySpaces/float(self.size))*100))

def chooseGenome(genomes):
	ranges = {}
	offset = 0
	for g in genomes:
		size = g.percent()
		if size > 0:
			start = offset
			end = start+size-1
			offset+= size
			ranges[g] = (start, end)

	#print ranges.values()

	chosenNumber = randint(0,offset-1)
	#print chosenNumber
	for genome in ranges:
		if ranges[genome][0] <= chosenNumber and chosenNumber <= ranges[genome][1]:
			return genome

def createGenomes():
	gn = genomeNames =	 ["Buchnera aphidicola APS ",
		"Escherichia coli K12 ",
		"Haemophilus influenzae Rd ",
		"Pseudomonas aeruginosa PA01 ",
		"Pasteurella multocida Pm70",
		"Salmonella typhimurium LT2 ",
		"Vibrio cholerae ",
		"Wigglesworthia glossinidia brevipalpis",
		"Xanthomonas axonopodis pv. citri 306  ",
		"Xanthomonas campestris ",
		"Xylella fastidiosa 9a5c ", 
		"Yersinia pestis CO_92",	
		"Yersinia pestis KIM5 P12 "]

	gs = genomeSizes = [569,4226,1725,5592,2034,4244,3841,659,4232,4068,2705,3633,3919]

	go = genomeOrphans = [24, 589, 187, 2271, 295, 601, 1414, 67, 542, 387, 815, 128, 335]

	genomes = [genome(gn[i], gs[i], go[i]) for i in range(13)]

	return genomes
