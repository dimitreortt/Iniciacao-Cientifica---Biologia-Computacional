import MOops.resultsOps as rops
from MOops.backlog import BackLog
#from backlog import LastSix
#from backlog import NewValue
class Results():
	def __init__(self, procNumber):
		#self.globalResults eh um dicionario
		self.globalResults = {}
		self.backlog = BackLog('proc%d' % procNumber)

	def update(self, lastSix):
		#print lastSix
		#getLocalResults faz calculo de numCIs e retorna uma lista com 6 duplas
		#(numCIs, listOfCIs),  os resultados
		localResults = rops.getLocalResults(lastSix)
		#print localResults
		assert len(localResults) == 6
		for item in localResults:
			assert item[0] > 27

		#print localResults
		#exit()
		#localFmly = getFmly(localResults)

		for (numCIs, listOfCIst) in localResults:
			if numCIs in self.globalResults:
				self.globalResults[numCIs] += 1
			else:
				print ('\n\nnovo numero de CIs encontrado #*#, Results.update ----> %d\n\n' % numCIs)
				#escreve no backlog
				self.backlog.store(lastSix, numCIs)
				self.globalResults[numCIs] = 1
				#print self.backlog

			print (self.globalResults) #, self.backlog.name)

	def gather(self, dic):
		for item in self.globalResults:
			if item in dic:
				dic[item] += self.globalResults[item]
			else:
				dic[item] = self.globalResults[item]

		return dic

	def writeBacklog(self, backLogOut):
		#blfile eh um arquivo que ja vem aberto
		self.backlog.write(backLogOut)
		

	def finish():
		print ('have something to be done')
		exit()
