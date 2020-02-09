import sys
import os
from mpi4py import MPI
#from modeOne_paralelo_ops import *
import MOops.modeOne_paralelo_ops as ops
import MOops.results as results
import subprocess as s

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if len(sys.argv) < 3:
	if rank == 0:
		print ('expected inputFile as the last parameter and tp number, exiting...')

	exit()
	
	
#rank = 0
if rank == 0:
	 print ('o numero de comm.size eh: %d'  % size)
	 outputDir = os.getcwd().replace('drivers', 'saidas/losangos/')
	 pathToInput = sys.argv[-1]
         print(pathToInput)
	 #genome name
	 
	 gName = pathToInput.split('/')[-1]
	 #alterar ops.newAlphaList() - done
	 alphaList, genoma1, genoma2 = ops.newAlphaList(pathToInput)
	 struc = (alphaList, genoma1, genoma2)

else:
		struc = None

if rank%20 == 0:
	print(rank)
#exit()
struc = comm.bcast(struc, root=0)
alphaList, genoma1, genoma2 = struc
#match1, match2, match3, match4, match5, match6, match7 = [getcm(alpha) for alpha in alphaList]
alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7, alpha8, alpha9 = alphaList

allFirsts = []
if rank == 0:
		startTime = ops.time.time()

		#alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7 = alphaList
		#alpha1, alpha2, alpha9, alpha10 = alphaList
		#lastSix = []
		count = 0
		'''print '\n\n',alpha1.possib, '1----\n\n'
		print '\n\n',alpha2.possib, '2----\n\n'
		print '\n\n',alpha3.possib, '3----\n\n'
		print '\n\n',alpha4.possib, '4----\n\n'
		print '\n\n',alpha5.possib, '5----\n\n'''
		#exit()
		for match1 in alpha1.possib:
		#for match1 in ops.getcm(alpha1):
			#print ops.getcm(alpha1)
			for match2 in alpha2.possib:
			#for match2 in ops.getcm(alpha2):
				for match3 in alpha3.possib:
				#for match3 in ops.getcm(alpha3):
					for match4 in alpha4.possib:
					#for match4 in ops.getcm(alpha4):
						#matching = ops.newMatching(match1, match2, match3, match4)
						#matching = [match1, match2, match3, match4]
						allFirsts.append([match1, match2, match3, match4])
						#print '\n\n%r\n\n' % allFirsts
						#allFirsts = [[m1,m2,m3,m4], [m1,m2,m3,m4], [m1,m2,m3,m4], [m1,m2,m3,m4], [m1,m2,m3,m4].........., [m1,m2,m3,m4]] <- 6**4 desses
						#print count
						count += 1
						#print count, 'here'
					#exit()
		#print len(allFirsts)
		

		#MARKER: ATE AQUI ESTA IDILICO DE PERFEITO!
		

		allFirsts = ops.organize(allFirsts, size)
		#for item in allFirsts:
		#	print len(item)
		
		#print len(allFirsts)
		assert len(allFirsts) == size
		print len(allFirsts[0])
		#assert len(allFirsts[0]) == pow(6,4)/size
		assert type(allFirsts[0]) == type([])
		print type(allFirsts[0])

		for alpha in alphaList:
			#print alpha
			pass
		print 'all asserted'

#exit()
allFirsts = comm.scatter(allFirsts, root=0)

myResults = results.Results(rank)
comm.barrier()

comm.barrier()
myTimes = []
#outFile = open('throuhPuts/throughPut%s'%sys.argv[-2], 'a+')
#backlog = BackLog('proc%d' % rank)
for curFirst in allFirsts:
	for match5 in alpha5.possib:
		for match6 in alpha6.possib:
			for match7 in alpha7.possib:
				for match8 in alpha8.possib:
					lastSix = []
					for match9 in alpha9.possib:
						cur = []
						cur = [match5, match6, match7, match8, match9]
						assert len(cur) == 5
						cur.extend(curFirst)
						assert len(cur) == 9
						lastSix.append(cur)
					myResults.update(lastSix)
#					#outFile.write("%f\n\n"%ops.time.time())
					myTimes.append(ops.time.time())
				assert len(myTimes) == 6
				print '+6, proc%d' % rank
				break
			break
		break
	break

allTimes = comm.gather(myTimes, root=0)
##Saidas todas ja armazenadas nos devidos arquivos de saida
comm.barrier()
if rank == 0:
	outFile = open('throuhPuts/throughPut%s'%sys.argv[-2], 'w')
	for myTimes in allTimes:
		assert len(allTimes) * len(myTimes) == size*6
		for time in myTimes:
			outFile.write("%f\n\n" % time)

	outFile.close()
	print "Saidas todas ja armazenadas nos devidos arquivos de saida"	
	s.call(['python', 'extractAvg.py', sys.argv[-2]])