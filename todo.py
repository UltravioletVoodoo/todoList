from tasks import tasks

import re
import os

def start():
	taskList = tasks()
	command = ""
	
	while(True):
		print("[HELPER]>", end = " ")
		usrInput = input("")
		
		
		action = re.match(r"add\s*(.*)\s*to\s*(\d+)", usrInput, re.I)
		if (action):
			taskList.addStep(action.group(2), action.group(1)) 
			continue
			
		action = re.match(r"add\s*(.*)", usrInput, re.I)
		if (action):
			taskList.addTask(action.group(1)) 
			continue
		
		action = re.match(r"pop\s*from\s*(\d+)", usrInput, re.I)
		if (action):
			taskList.popStep(action.group(1))
			continue
		
		action = re.match(r"pop", usrInput, re.I)
		if (action):
			taskList.popTask() 
			continue
			
		action = re.match(r"print", usrInput, re.I)
		if (action):
			taskList.printTasks() 
			continue
			
		action = re.match(r"^clear$|^cls$", usrInput, re.I)
		if (action):
			os.system('cls')
			continue
		
		action = re.match(r"^q$|^exit$", usrInput, re.I)
		if (action):
			print("Bye bye") 
			break
		
		print(usrInput + "->" + usrInput)
		
	
start()