import os

dir1 = "/home/vanrao/Trialdata/DPSWorkshop/"
outputDir = "/home/vanrao/Trialdata/DPSWorkshopOpcodeFiles/"
for file1 in os.listdir("/home/vanrao/Trialdata/DPSWorkshop/"):
	inputFile = dir1+file1
	outputFile = outputDir+file1
	os.system("node readFile.js "+inputFile+" "+outputFile)
