import os
import getTreeEditdistScore
import getTreeEditDistanceMin


#csvdata = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/'
csvdata = "/home/vanrao/Trialdata/Level_1_Scores/"
level2file = '/home/vanrao/Trialdata/Level_2_Scores/'

filePath = "/home/vanrao/Trialdata/FinalOpcodes/"
files = os.listdir("/home/vanrao/Trialdata/FinalOpcodes/")
for i in range(len(files)):
	getTreeEditdistScore.count = 0
	getTreeEditdistScore.startTime = 0
	getTreeEditdistScore.tree = ''
	getTreeEditdistScore.treeList = []
	getTreeEditdistScore.level1List = []
	#if(files[i] == 'Tanay.txt'):
	newf = files[i].replace(".txt", "")
	print csvdata+newf+".csv"
	print level2file+newf+".csv"
	getTreeEditdistScore.createCsvs(csvdata+newf+".csv", level2file+newf+".csv", filePath+files[i])
	#getTreeEditDistanceMin.createCsvs(csvdata+newf+"Min"+".csv", level2file+newf+"Min"+".csv", filePath+files[i])
	#break
	#i=i+1

