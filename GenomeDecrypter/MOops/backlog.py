#NewValue eh um valor encontrado nos calculos de numCIs 
#que ainda nao havia sido encontrado, o nome faz sentido
#porem pode ser confuso
class NewValue():
	def __init__(self,lastSix, name):
		self.name = name
		self.lastSix = lastSix

	def __str__(self):
		print (self.lastSix)
		return ''

	def write(self, file):
		file.write('Novo valor: %r\n\'Ultimos\' 6 MMs:\n' % self.name)
		for lista in self.lastSix:
			file.write('%r\n' % lista)
		file.write('\n')

class BackLog():
	def __init__(self,name):
		#BackLog tem um nome, correspondente ao numero do processador
		self.name = name
		self.newValues = []
		self.seenValues = []

	def __str__(self):
		print ('Os itens armazenados no backlog de %r sao:' % self.name)
		for item in self.newValues:
			print (item)
		return ''

	#def store(self, listOfCis, numOfCIs):
	def store(self, lastSix, newNumber):
		self.newValues.append(NewValue(lastSix, newNumber))
		self.seenValues.append(newNumber)

	def write(self, file):
		for value in self.newValues:
			value.write(file)

#if curNumberOfCIs not in backlog.seenValues:
	#backLog.store(lastSix, curNumberOfCIs)
