from mpi4py import MPI
from func import collectAllGeneMatchings as cm

def getcm(alpha):
	#return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
	return [[[1,2], [2,3]], [[1,3],[2,2]]]

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	for match1 in getcm(1):
		for match2 in getcm(1):
			for match3 in getcm(1):
				data = []
				data.extend([match1, match2, match3])
				print data
				
else:
    data = None
data = comm.scatter(data, root=0)
print data
for match4 in getcm(1):
	data.append(match4)
print data

#assert data == 'o'
#print func('love')