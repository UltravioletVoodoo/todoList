from task import task

class tasks:
	
	def __init__(self):
		self.taskList = []
		self.taskIndex = 1
	
	def addTask(self, name):
		self.taskList.append(task(name, self.taskIndex))
		self.taskIndex = self.taskIndex + 1
		
	def popTask(self):
		if (len(self.taskList) == 0):
			print("No tasks to pop")
		else:
			self.taskList.pop()
			self.taskIndex = self.taskIndex - 1
		
	def addStep(self, index, name):
		if (self.taskList[int(index) - 1] is not None):
			self.taskList[int(index) - 1].addStep(name)
		else:
			print("No task with index '" + index + "' found")
			
	def popStep(self, index):
		if (self.taskList[int(index) - 1] is not None):
			self.taskList[int(index) - 1].popStep()
		else:
			print("No task with index '" + index + "' found")
			
	def printTasks(self):
		for x in self.taskList:
			x.printTask()