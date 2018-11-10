from tasks import tasks

import re
import os

def start():
	taskList = tasks()
	command = ""
	
	while(True):
		print("[HELPER]>", end = " ")
		usrInput = input("")
		
		
		action = re.match("add\s*(.*)\s*to\s*(\d*)", usrInput, re.I)
		if (action):
			taskList.addStep(action.group(2), action.group(1)) 
			continue
			
		action = re.match("add\s*(.*)", usrInput, re.I)
		if (action):
			taskList.addTask(action.group(1)) 
			continue
		
		action = re.match("pop\s*from\s*(\d*)", usrInput, re.I)
		if (action):
			taskList.popStep(action.group(2)) 
			continue
		
		action = re.match("pop\s*(.*)", usrInput, re.I)
		if (action):
			taskList.popTask() 
			continue
			
		action = re.match("print", usrInput, re.I)
		if (action):
			taskList.printTasks() 
			continue
			
		action = re.match("^clear$|^cls$", usrInput, re.I)
		if (action):
			os.system('cls')
			continue
		
		action = re.match("^q$|^exit$", usrInput, re.I)
		if (action):
			print("Bye bye") 
			break
		
		print(usrInput + "->" + usrInput)
		
	
start()