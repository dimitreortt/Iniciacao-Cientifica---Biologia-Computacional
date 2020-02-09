import sys
import os
from os import listdir
from os.path import isfile, join
import build

if __name__ == '__main__':

	curDir = os.getcwd()
	inputDir = curDir.replace('drivers', 'genomasDeInput/')#+'/genomasDeInput'

	listOfGenomes = [f for f in listdir(inputDir) if isfile(join(inputDir, f))]
	
	for genome in listOfGenomes:

		sys.argv.insert(1,genome)
		print('Now executing for %s\n\n' % genome)

		if genome == 'genoma8':
			build.buildLosangos(inputDir+genome)
			exit()
		
		#exit()
		#build.runMyHeu(curDir)
		#build.run3Heus(curDir, genome)
		#build.runGurobi(curDir, genome)
		print ('Finished executing for %s\n\n' % genome)
