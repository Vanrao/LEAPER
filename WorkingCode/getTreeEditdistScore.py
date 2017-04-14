import os
import csv

# can only be written into files
#global tree
tree = ''
treeList = []
solutionsListForLevel1 = ["{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps450{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}", 
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps360{turnleft90{movesteps360{movesteps10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{movesteps360{turnleft90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps390{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{moveX380{movesteps350{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps100{movesteps100{movesteps50{moveX100{moveX100{moveX100{moveX50{moveX10{moveX10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps100{movesteps100{movesteps50{moveX100{moveX100{moveX100{moveX50{moveX10{moveX10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps420{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps70{movesteps250{movesteps60{pointindirection90{movesteps100{movesteps100{movesteps100{movesteps49{movesteps20{movesteps30{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps90{movesteps170{pointindirection90{movesteps90{movesteps90{movesteps90{movesteps20{movesteps50{movesteps20{movesteps20{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{pointindirection180{movesteps100{movesteps100{movesteps100{movesteps20{movesteps30{pointindirection90{movesteps100{movesteps90{movesteps100{movesteps90{pointindirection90{movesteps10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}{if<key[downarrow]pressed>then{pointindirection30{movesteps10}}}}}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{movesteps350{turnleft90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps10{movesteps100{movesteps10{movesteps100{movesteps10{movesteps10{movesteps10{movesteps10{pointindirection90{movesteps90{movesteps10{movesteps10{movesteps10{movesteps100{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{movesteps10{pointindirection90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{turnleft90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps320{pointindirection90{movesteps420{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps360{pointindirection90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps390{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps375{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection90{movesteps350{moveX200{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{movesteps10{movesteps10{movesteps10{movesteps100{movesteps100{movesteps100{movesteps10{pointindirection90{movesteps100{movesteps100{movesteps100{movesteps10{movesteps10{movesteps10{movesteps10{movesteps10{movesteps10{movesteps10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps375{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps370{pointindirection90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps50{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{turnleft90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps356{pointindirection90{movesteps380{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps70{movesteps250{movesteps60{pointindirection90{movesteps100{movesteps100{movesteps100{movesteps49{movesteps20{movesteps30{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}"
]
solutionsListForLevel2 = []
print len(solutionsListForLevel1)
def createCsvs(studentCsv1, studentCsv2, studentInputFile):
	studentScores = studentCsv1
	studLevel2 = studentCsv2
	#tree format input text file of student block data
	fileName = studentInputFile
	tempFile = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/temp.txt'

	#correct solns-Level-1
	fullPath = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/CorrectSolutions/"
	corrSolns = os.listdir("/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/CorrectSolutions/")
	#for eachFile in corrSolns:
	
	#correct solns for level-2 ana level-3
	secPath = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/OurSoln_level2.txt"
	solutionsListForLevel2.append(secPath)

	#for solution 1
	ff = open(studentScores, 'w')
	level2file = open(studLevel2, 'w')
	def csvwrite(timestamp, score):
		csvwriter = csv.writer(ff, delimiter=',')
		csvwriter.writerow([timestamp, score[0], score[1], score[2], score[3], score[4], score[5], score[6], score[7], score[8], score[9], score[10], score[11], score[12], score[13], score[14], score[15], score[16], score[17], score[18], score[19], score[20], score[21], score[22], score[23],score[24], score[25], score[26], score[27]])
		#csvwriter.writerow([levelNum, timestamp,str(score)])
	def csvwrite2(timestamp, score):
		csvwriter = csv.writer(level2file, delimiter=',')
		csvwriter.writerow([timestamp,  score[0]])
		#csvwriter.writerow([levelNum, timestamp,str(score)])


	def isInt(s):
		try: 
		    int(s)
		    return True
		except ValueError:
		    return False


	def calcScore(studentSoln, listOfCorrectSolns):
		scoresOrder = []
		studentSoln = studentSoln.replace("<","")
		studentSoln = studentSoln.replace(">","")
		studentSoln = studentSoln.replace("[","")
		studentSoln = studentSoln.replace("]","")
		for eachSoln in listOfCorrectSolns:
			eachSoln = eachSoln.replace("<","")
			eachSoln = eachSoln.replace(">","")
			eachSoln = eachSoln.replace("[","")
			eachSoln = eachSoln.replace("]","")
			score = os.popen("java -jar RTED_v1.1.jar -t"+" "+studentSoln+" "+eachSoln, "r")
			#print score.read()
			scoresOrder.append(score.read().rstrip())
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
			#with open(tempFile, 'w') as temp:
			#	temp.write(treeStructure)
			if(levelNum == 'Level 1'):
				#print 'Level1'
				treeScores = calcScore(treeStructure, solutionsListForLevel1)
				#print timestamp+":"+str(treeScore)
				csvwrite(timestamp, treeScores)
				#open(tempFile, 'w').close()
				#print "\n"
			elif(levelNum == 'Level2'):
				pass
				'''
				treeScores = calcScore(treeStructure,solutionsListForLevel2)
				#print timestamp+":"+str(treeScore)
				csvwrite2(timestamp, treeScores)
				open(tempFile, 'w').close()
				#print "\n"'''
			
			
		elif(len(treeData)==2):
			pass
			'''timestamp = treeData[0]
			treeStructure = treeData[1]
			#with open(tempFile, 'w') as temp:
			#	temp.write(treeStructure)
			treeScores = calcScore(treeStructure, solutionsListForLevel1)
			#print timestamp+":"+str(treeScore)
			csvwrite(timestamp, treeScores)
			open(tempFile, 'w').close()
			#print "\n"'''
		
	


