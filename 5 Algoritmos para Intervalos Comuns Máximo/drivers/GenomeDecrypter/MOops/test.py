
import sys
from mpi4py import MPI
#from modeOne_paralelo_ops import *
import modeOne_paralelo_ops as ops
import results

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	 pathToInput = sys.argv[1]
	 #alterar ops.newAlphaList()
	 alphaList, genoma1, genoma2 = ops.newAlphaList(pathToInput)
	 struc = (alphaList, genoma1, genoma2)

else:
		struc = None

result = results.Results(rank)
result.globalResults[rank] = rank*rank
result.globalResults[rank+1] = rank*rank
result.backlog.store([[1]], 'namename')

finalResults = comm.gather(result, root=0)
if rank == 0:

	losangoAll = ops.gatherLosangos(finalResults)

	losangoFile = open('%s_losango'%sys.argv[1], 'w')
	losangoFile.write('Losango resultante de %s\n\nnumCIs\tqtdPresencas\n' % (sys.argv[1]))

	for item in losangoAll:
		losangoFile.write('%r\t%r\n' % (item, losangoAll[item]))

	backLogOutfile = open('backlog_%s'%sys.argv[1], 'w')
	for result in finalResults:
		result.writeBacklog(backLogOutfile)
