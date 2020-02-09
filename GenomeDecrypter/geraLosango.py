import sys
import os
from geraLosangoOperations import runFindAllMatchings, getPaths

if __name__ == '__main__':
	curDir = os.getcwd()
	print ('heu')
	#pathToInput, inputPath, inputName = getPaths(curDir)
	print (sys.argv)
	#exit()
	#argv deve estar: ['geraLosango.py', '../inputDir/inputname']
	inputPath = sys.argv[1]
	print (inputPath)
	# exec(findAllMatchings.py)
	print ('to aquias')
	runFindAllMatchings(inputPath)

	exit()