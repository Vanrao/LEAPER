import os
import getTreeEditdistScore

i=1
#csvdata = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/'
csvdata = "/home/vanrao/Trialdata/Level_1_Scores/"
level2file = '/home/vanrao/Trialdata/Level_2_Scores/'

filePath = "/home/vanrao/Trialdata/FinalOpcodes/"
files = os.listdir("/home/vanrao/Trialdata/FinalOpcodes/")
for i in range(len(files)):
	newf = files[i].replace(".txt", "")
	print csvdata+newf+".csv"
	print level2file+newf+".csv"
	if(i==6):
		getTreeEditdistScore.createCsvs(csvdata+newf+".csv", level2file+newf+".csv", filePath+files[i])
		break
	#i=i+1

