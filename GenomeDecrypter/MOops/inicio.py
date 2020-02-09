from mpi4py import MPI
def func():
	print 10
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	f = func
	f()
    data = {'a': 7, 'b': 3.14}
    print 'antes'
    req = comm.isend(data, dest=1, tag=11)
    
    #req.wait()
    
elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()    
    print 'what', req
    