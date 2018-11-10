from step import step

class task:

	def __init__(self, name, index):
		self.name = name
		self.index = index
		self.steps = []
		self.stepIndex = 1
		
	def addStep(self, stepString):
		self.steps.append(step(stepString, self.stepIndex))
		self.stepIndex = self.stepIndex + 1
		
	def popStep(self):
		if (len(self.steps) == 0):
			print(self.name + " has no steps to pop")
		else:
			self.steps.pop()
			self.stepIndex = self.stepIndex - 1
			
	def printTask(self):
		print(str(self.index) + ". " + self.name)
		
		if (len(self.steps) == 0):
			print("    " + self.name + " has no steps")
		
		for x in self.steps:
			x.printStep()