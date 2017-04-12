#import getData
import os
import getData

inputFileDir = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/DPSWorshopDataOpcodesFiles/"
opcodesFileDir = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/OpcodeReqdData/"
treeInputsFileDir = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/FinalOpcodes/"

files = os.listdir("/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/DPSWorshopDataOpcodesFiles/")

for path in files:
	file1 = inputFileDir+path
	file2 = opcodesFileDir+path
	file3 = treeInputsFileDir+path
	getData.create(file1, file2, file3)
'''
file1 = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/DPSWorshopDataOpcodesFiles/16_input.txt"
file2 = "hhh.txt"
file3 =  "ddd.txt"

getData.create(file1, file2, file3)'''

