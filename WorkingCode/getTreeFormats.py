#import getData
import os
import getData


inputFileDir = "/home/vanrao/Trialdata/DPSWorkshopOpcodeFiles/"
opcodesFileDir = "/home/vanrao/Trialdata/OpcodeReqdData/"
treeInputsFileDir = "/home/vanrao/Trialdata/FinalOpcodes/"

files = os.listdir("/home/vanrao/Trialdata/DPSWorkshopOpcodeFiles/")

for path in files:
	getData.prevStr = "";
	getData.newStr = "";
	getData.start = 0;
	getData.count = 0;
	getData.motion_goto = 0;
	getData.motion_gotoxy = 0;
	file1 = inputFileDir+path
	file2 = opcodesFileDir+path
	file3 = treeInputsFileDir+path
	getData.create(file1, file2, file3)


'''
file1 = "/home/vanrao/Desktop/14_input.txt"
file2 = "hhh.txt"
file3 =  "ddd.txt"

getData.create(file1, file2, file3)
'''

