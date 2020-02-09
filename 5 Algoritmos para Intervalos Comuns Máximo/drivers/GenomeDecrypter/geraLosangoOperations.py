import sys
import os
from findAllMatchings import findAllMatchings

def getPaths(curDir):
	paths = curDir.split('/')
	print (curDir)
	exit()
	paths[-2] = 'genomasDeInput/'
	paths.pop(-1)
	inputPath = '/'.join(paths)
	inputName = sys.argv[1]

	pathToInput = inputPath+inputName
	return pathToInput, inputPath, inputName

def runFindAllMatchings(pathToInput):	
	#sys.argv.extend([pathToInput, 'keyword'])
	#sys.argv[1], sys.argv[2] = pathToInput, 'keyword'
	#execfile('findAllMatchings.py')
	findAllMatchings(pathToInput)


def getFmly(results):
	fmly = {}
	# create dictionary {gene family : positions of family in genome}
	for idx, itm in enumerate(results):
	    if(itm not in fmly):
	        fmly[itm] = [idx]
	    else:
	        fmly[itm].extend([idx])

	return fmly

def getOutPath(curDir):
	paths = curDir.split('/')
	paths[-2] = 'saidas'
	paths[-1] = 'losangos/'
	outPutPath = '/'.join(paths)
	outName = sys.argv[1] + '_losango'

	return outPutPath + outName