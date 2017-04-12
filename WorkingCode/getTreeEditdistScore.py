import os
import csv

# can only be written into files
#global tree
tree = ''
treeList = []
solutionsListForLevel1 = []
solutionsListForLevel2 = []

def createCsvs(studentCsv, studentInputFile):
	studentScores = studentCsv
	#tree format input text file of student block data
	fileName = studentInputFile
	tempFile = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/temp.txt'

	#correct solns-Level-1
	fullPath = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/CorrectSolutions/"
	corrSolns = os.listdir("/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/CorrectSolutions/")
	for eachFile in corrSolns:
		solutionsListForLevel1.append(fullPath + eachFile)
	
	#correct solns for level-2 ana level-3
	secPath = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/OurSoln_level2.txt"
	solutionsListForLevel2.append(secPath)

	#for solution 1
	ff = open(studentScores, 'w')
	def csvwrite(levelNum, timestamp, score):
		csvwriter = csv.writer(ff, delimiter=',')
		csvwriter.writerow([levelNum, timestamp,str(score)])


	def isInt(s):
		try: 
		    int(s)
		    return True
		except ValueError:
		    return False


	def calcScore(studentSoln, listOfCorrectSolns):
		scoresOrder = []
		for eachSoln in listOfCorrectSolns:
			score = os.popen("java -jar RTED_v1.1.jar -f"+" "+studentSoln+" "+eachSoln+" "+"-s left", "r")
			#print score.read()
			scoresOrder.append(score.read())
		return scoresOrder

	with open(fileName,'r') as f:
		data = f.read().splitlines()
	#print data
	for eachData in data:
		global tree
		if(eachData != ''):
			if(isInt(eachData) or ('Level' in eachData)):
				tree = tree + eachData+','
			else:
				tree = tree + eachData
		else:
			treeList.append(tree)
			tree = ''

	#print treeList
	for item in treeList:
		treeData = item.split(',')
		if(len(treeData) == 3):
			levelNum = treeData[0]
			timestamp = treeData[1]
			treeStructure = treeData[2]
			with open(tempFile, 'w') as temp:
				temp.write(treeStructure)
			if(levelNum == 'Level 1'):
				#print 'Level1'
				treeScores = calcScore(tempFile, solutionsListForLevel1)
				#print timestamp+":"+str(treeScore)
				csvwrite(levelNum, timestamp, treeScores)
				open(tempFile, 'w').close()
				#print "\n"
			elif(levelNum == 'Level2'):
				treeScores = calcScore(tempFile,solutionsListForLevel2)
				#print timestamp+":"+str(treeScore)
				csvwrite(levelNum, timestamp, treeScores)
				open(tempFile, 'w').close()
				#print "\n"
			
			
		elif(len(treeData)==2):
			timestamp = treeData[0]
			treeStructure = treeData[1]
			with open(tempFile, 'w') as temp:
				temp.write(treeStructure)
			treeScores = calcScore(tempFile, solutionsListForLevel1)
			#print timestamp+":"+str(treeScore)
			csvwrite('NA', timestamp, treeScores)
			open(tempFile, 'w').close()
			#print "\n"
		
	

