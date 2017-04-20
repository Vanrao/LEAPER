import os
import getTreeEditdistScore
import getTreeEditDistanceMin


#csvdata = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/'
csvdata = "/home/vanrao/Trialdata/Level_1_Scores/"
#level2file = '/home/vanrao/Trialdata/Level_2_Scores/'
minFuture = "/home/vanrao/Trialdata/MinAtEveryTimestamp/"

filePath = "/home/vanrao/Trialdata/FinalOpcodes/"
files = os.listdir("/home/vanrao/Trialdata/FinalOpcodes/")
for i in range(len(files)):
	getTreeEditdistScore.count = 0
	getTreeEditdistScore.startTime = 0
	getTreeEditdistScore.tree = ''
	getTreeEditdistScore.treeList = []
	getTreeEditdistScore.level1List = []
	getTreeEditdistScore.firstTime = 0
	getTreeEditdistScore.level2List = []
	#if(files[i] == '3_input.txt'):
	getTreeEditDistanceMin.count = 0
	getTreeEditDistanceMin.startTime = 0
	getTreeEditDistanceMin.tree = ''
	getTreeEditDistanceMin.treeList = []
	getTreeEditDistanceMin.level1List = []
	getTreeEditDistanceMin.firstTime = 0
	getTreeEditDistanceMin.level2List = []
	#if(files[i] == '8_input.txt'):
	newf = files[i].replace(".txt", "")
	print csvdata+newf+".csv"
	#print level2file+newf+".csv"
	#print minFuture+newf+".csv"
	getTreeEditdistScore.createCsvs(csvdata+newf+".csv", filePath+files[i])
	#getTreeEditDistanceMin.createCsvs(minFuture+newf+".csv", filePath+files[i])
	#break
	#i=i+1

