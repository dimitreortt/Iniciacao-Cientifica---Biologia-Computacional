from Header_geraGenomas import *
from familia_h import *
from genoma_h import *
from random import shuffle

if __name__ == "__main__":
	
	#findSolutionForLinearSystem()

	#cria todos os 13 genomas
	genomes = createGenomes()

	numero_total_genes = 41447

	#cria todas as familias de genes
	families = createFamilies()

	atributeOrphans(families, genomes)

	startSize9(families, genomes)
	startSize10(families, genomes)
	startSize11(families, genomes)
	startSize12(families, genomes)
	startSize13(families, genomes)

	#cria banco de genes
	allGenes = createGeneBank(families)

	#distribui os genes entre os genomas
	while len(allGenes) > 0:
		#chosenGenome = chooseGenome(genomes)
		#genePosition = randint(len(allGenes))

		chooseGenome(genomes).insertGene(allGenes.pop(randint(0, len(allGenes)-1)))
		#print len(allGenes)
		#chosenGenome = chooseGenome(genomes)
		#exit()
		#gene = allGenes[randint(len(allGenes))]
		#chosenGenome.insert(gene)
		#allGenes.pop(gene)

	saveOutput(families, genomes)


	#for i in range(13):
		#genomas[i].name = genomaNames[i]


'''TAAA, umasceu pronto.. ok. Agora  hora de mexer o terceiro grco (e por fim a tabela do artigo do angibauld) 

no terceiro go eu vou fazer assim: pego os 41k genes que gerei no grfico1 e distribuo eles aleatamente proporcionalmente nos 13 genomas,
o que seria isso? distribuir proporcionalmente significa respeitar a sua proporo de espao livre, por exemplo, 1 genoma pode ter 
1000 espaos livres enquanto outro s tem 200 e mesmo assim o que tem menos ainda recebe o prximo gene, pois 200 espaos pode
significar mais nesse genoma que no outro, ento, em cada distribuio, eu dou um peso  aleatoriedade da escolha, proporcional a quantidade de  
espaos livres de cada genoma.


1.
1.1Gere soma 
1.2chute um valor dentro dessa soma
2. verifique a quem pertence esse valor
3. insira o gene nesse genoma'''