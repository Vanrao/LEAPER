import os
import getTreeEditdistScore

csvdata = "/home/vanrao/Trialdata/Level_1_Scores/"
level2file = '/home/vanrao/Trialdata/Level_2_Scores/'

filePath = "/home/vanrao/Trialdata/FinalOpcodes/"
files = os.listdir("/home/vanrao/Trialdata/FinalOpcodes/")
for i in range(len(files)):
	formattedName = files[i].replace(".txt", "")
	print csvdata+formattedName+".csv"
	print level2file+formattedName+".csv"
	getTreeEditdistScore.createCsvs(csvdata+formattedName+".csv", level2file+formattedName+".csv", filePath+files[i])

print "Done writing into files"

