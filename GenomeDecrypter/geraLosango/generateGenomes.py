import random
import sys

def findPosition(lista):
	position = random.randint(0,size-1)
	if lista[position] != "":
		while(lista[position] != ""):
			position = random.randint(0,size-1)

	return position

numGenes = int(sys.argv[2])

size = numGenes*3

genoma1 = ["" for i in range(size)]
genoma2 = ["" for i in range(size)]

for i in range(1,4):
	for j in range(1,numGenes+1):
		genoma1[findPosition(genoma1)] = j

for i in range(1,4):
	for j in range(1,numGenes+1):
		genoma2[findPosition(genoma2)] = j

print genoma1, genoma2

print sys.argv
#folderName = sys.argv[0].split('/')[-3]
#myfile = open('%s/%s' % (folderName, sys.argv[1]), 'w')
myfile = open('tamanho%s/%s' % (sys.argv[2],sys.argv[1]), 'w')
myfile.write('%s\n%s' % (' '.join([str(item) for item in genoma1]), ' '.join([str(item) for item in genoma2])))
