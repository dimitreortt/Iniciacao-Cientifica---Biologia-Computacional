import subprocess as sp
import shlex
from CollectGeneMatchings import recoverStrings
from time import time
import copy
import sys
import os

def buildLosangos(inputPath):
	cpy = copy.deepcopy(sys.argv)

	tempos = open('buldingLosangos_Tempos', 'a+')
	inicio = time()
	#os.chdir(os.getcwd()+'/geraLosango')

	#execfile('geraLosango.py')
	sp.call(['python','geraLosango.py', inputPath])
	#os.chdir(curDir)

	tempos.write('Tempo para contruir losango de %s: %f' % (sys.argv[1], time()-inicio))
	tempos.close()

	sys.argv = cpy

def runMyHeu(curDir):
	print ('Now executing MyHeuristic \n\n')
	os.chdir(os.getcwd()+'/minhaHeuristica/')
	sys.argv.append('100')
	execfile('driverHeuristica.py')
	sys.argv[2] = ('500')
	execfile('driverHeuristica.py')
	os.chdir(curDir)
	sys.argv.pop(-1)

def runILCS(curDir):	
	print ('Now executing ILCS \n\n')
	execfile('ILCS.py')
	os.chdir(curDir+'/3heuristicas/')
	print ('Finished ILCS for %s' % sys.argv[1])

def runIILCS(curDir):
	print ('Now executing IILCS \n\n')
	execfile('IILCS.py')
	os.chdir(curDir+'/3heuristicas/')
	print ('Finished IILCS for %s' % sys.argv[1])

def runHYB(curDir):
	print ('Now executing HYB \n\n')
	execfile('HYB.py')
	os.chdir(curDir+'/3heuristicas/')
	print ('Finished HYB for %s' % sys.argv[1])

def run3Heus(curDir, inputName):
	#estabelecendo diretorios para execucao
	os.chdir(curDir+'/3heuristicas/')
	sys.argv[1] = '%s' % (curDir+'/genomasDeInput/'+inputName)	
	
	#execute as heuristicas
	runILCS(curDir)
	runIILCS(curDir)
	runHYB(curDir)

	#consertando entrada padrao para resto da execucao
	sys.argv[1] = inputName
	os.chdir(curDir)

def runGurobi(curDir, inputName):
	print ('Now executing ExactGurobi \n\n')
	os.chdir(os.getcwd()+'/gurobi/')
	#execfile('maxCI.py')
	#Nao rodar regra4!! Tenho 90% de certeza que a regra dada no artigo nao funciona!!
	subprocess.call(shlex.split('gurobi.sh maxCI.py %s 1 2 3' % (curDir+'/genomasDeInput/'+inputName)))

	#consertando entrada padrao para resto da execucao	
	sys.argv[1] = inputName
	os.chdir(curDir)
	print ('Finished ExactGurobi for %s' % sys.argv[1])
