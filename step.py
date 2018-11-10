class step:
	
	def __init__(self, stepString, index):
		self.stepString = stepString
		self.index = index
		
	def printStep(self):
		print("    " + str(self.index) + ". " + self.stepString)