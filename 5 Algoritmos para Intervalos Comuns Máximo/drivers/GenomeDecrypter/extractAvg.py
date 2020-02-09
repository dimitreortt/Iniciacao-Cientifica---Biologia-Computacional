import sys

times = open('throuhPuts/throughPut%s'%sys.argv[1], 'r').read().split()
times = [item for item in times if len(item) == len('1565460057.766179')]
print times[:160]
times.sort()
times = [float(times[i])-float(times[i-1]) for i in range(1,len(times))]
print times[:160]

count = 0
for i in reversed(times):
	count += 1
	if i <0:
		print count
		print i
		times.remove(i)
		print 	'huashduashd'

soma = sum(times)
print soma, len(times)
avg = (soma/len(times)/6)
print 'a media final eh:%f' % (soma/len(times)/6)
print 	'\nFinalizado com perfeito sucesso!'
