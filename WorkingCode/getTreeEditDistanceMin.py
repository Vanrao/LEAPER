import os
import csv


#global tree
tree = ''
firstTime = 0
treeList = []
level1List = []
level2List = []
solutionsListForLevel1 = ["{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps450{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}", 
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps360{turnleft90{movesteps360{movesteps10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{movesteps360{turnleft90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps390{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{moveX380{movesteps350{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps100{movesteps100{movesteps50{moveX100{moveX100{moveX100{moveX50{moveX10{moveX10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps100{movesteps100{movesteps50{moveX100{moveX100{moveX100{moveX50{moveX10{moveX10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps420{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps70{movesteps250{movesteps60{pointindirection90{movesteps100{movesteps100{movesteps100{movesteps49{movesteps20{movesteps30{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps90{movesteps170{pointindirection90{movesteps90{movesteps90{movesteps90{movesteps20{movesteps50{movesteps20{movesteps20{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{pointindirection180{movesteps100{movesteps100{movesteps100{movesteps20{movesteps30{pointindirection90{movesteps100{movesteps90{movesteps100{movesteps90{pointindirection90{movesteps10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}{if<key[downarrow]pressed>then{pointindirection30{movesteps10}}}}}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{movesteps350{turnleft90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps100{movesteps10{movesteps100{movesteps10{movesteps100{movesteps10{movesteps10{movesteps10{movesteps10{pointindirection90{movesteps90{movesteps10{movesteps10{movesteps10{movesteps100{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{movesteps10{pointindirection90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{turnleft90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps400{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps320{pointindirection90{movesteps420{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps360{pointindirection90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps390{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps375{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection90{movesteps350{moveX200{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps10{movesteps10{movesteps10{movesteps10{movesteps100{movesteps100{movesteps100{movesteps10{pointindirection90{movesteps100{movesteps100{movesteps100{movesteps10{movesteps10{movesteps10{movesteps10{movesteps10{movesteps10{movesteps10{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps375{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps370{pointindirection90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{pointindirection90{movesteps50{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps350{turnleft90{movesteps370{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}","{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps356{pointindirection90{movesteps380{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}",
"{root{whenbackdropswitchesto[level2]{hide{goto-195143}}}{whengreenflagclicked{goto-195203{show{pointindirection180{movesteps70{movesteps250{movesteps60{pointindirection90{movesteps100{movesteps100{movesteps100{movesteps49{movesteps20{movesteps30{Forever{if<touching[Stop]>then{switchbackdropto[level2]}}}}}}}}}}}}}}}}}}"
]
solutionsListForLevel2 = ['{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[downarrow]pressed>then{pointindirection165{movesteps5}}}{if<touching[Stop]>then{switchbackdropto[level3]}}}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{show{goto-195143}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}{touching[_edge_]>then}{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}{Forever{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}}{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<touching[Stop]>then{switchbackdropto[level3]}}}{Forever{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}}{Forever{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}}{Forever{if<touching[#aac612]>then}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143}}}{Forever{if<key[downarrow]pressed>then{pointindirection180{movesteps1}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps1}}}{if<key[uparrow]pressed>then{pointindirection0{movesteps1}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps1}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#ff0000]>then{playsound[8]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<touching[Stop]>then{switchbackdropto[level3]}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}}','{root{whengreenflagclicked{hide{goto-195143{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<touching[Stop]>then{switchbackdropto[level3]}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}}}}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}{playsound[0]}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}}}}}{If<>then}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}{if<touching[#ff0000]>then{playsound[0]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}}}}}{If<>then}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#000000]>then{playsound[dog1]}}{if<touching[#ff0000]>then{playsound[0]}}}}}','{root{whengreenflagclicked{hide}}{whenbackdropswitchesto[level1]{hide}}{whenbackdropswitchesto[level2]{show{goto-195143{Forever{if<key[uparrow]pressed>then{pointindirection0{movesteps10}}}{if<key[downarrow]pressed>then{pointindirection180{movesteps10}}}{if<key[leftarrow]pressed>then{pointindirection-90{movesteps10}}}{if<key[rightarrow]pressed>then{pointindirection90{movesteps10}}}}}}}{whenbackdropswitchesto[level3]{Forever{if<touching[#ff0000]>then{playsound[dog1]}}{if<touching[#000000]>then{playsound[4]}}}}}']
startTime = 0
count = 0
#print len(solutionsListForLevel1)
def createCsvs(studentCsv1, studentInputFile):
	studentScores = studentCsv1
	#studLevel2 = studentCsv2
	#tree format input text file of student block data
	fileName = studentInputFile
	tempFile = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/temp.txt'

	
	
	#for solution 1
	ff = open(studentScores, 'w')
	#level2file = open(studLevel2, 'w')
	
	def csvwrite(timestamp, score):
		csvwriter = csv.writer(ff, delimiter=',')
		global count
		global startTime
		if(count == 0):
			startTime = timestamp
			count = 1
			#print timestamp
			percentageTime = (int(timestamp)-int(startTime)) / 1000 ;
			#print percentageTime
			'''csvwriter.writerow([timestamp, score[0], score[1], score[2], score[3], score[4], score[5], score[6], score[7], score[8], score[9], score[10], score[11], score[12], score[13], score[14], score[15], score[16], score[17], score[18], score[19], score[20], score[21], score[22], score[23],score[24], score[25], score[26], score[27]])'''
			csvwriter.writerow([percentageTime,score])
		else:
			#print timestamp
			percentageTime = (int(timestamp)-int(startTime)) / 1000 ;
			#print percentageTime
			'''csvwriter.writerow([timestamp, score[0], score[1], score[2], score[3], score[4], score[5], score[6], score[7], score[8], score[9], score[10], score[11], score[12], score[13], score[14], score[15], score[16], score[17], score[18], score[19], score[20], score[21], score[22], score[23],score[24], score[25], score[26], score[27]])'''
			csvwriter.writerow([percentageTime,score])
	#def csvwrite2(timestamp, score):
	#	csvwriter = csv.writer(level2file, delimiter=',')
	#	csvwriter.writerow([timestamp,  score[0]])
		#csvwriter.writerow([levelNum, timestamp,str(score)])


	def isInt(s):
		try: 
		    int(s)
		    return True
		except ValueError:
		    return False


	def calcScore(studentSoln, listOfCorrectSolns):
		#print studentSoln
		#print "\n"
		#print listOfCorrectSolns
		scoresOrder = []
		studentSoln = studentSoln.replace("<","")
		studentSoln = studentSoln.replace(">","")
		studentSoln = studentSoln.replace("[","")
		studentSoln = studentSoln.replace("]","")
		#print studentSoln
		for eachSoln in listOfCorrectSolns:
			eachSoln = eachSoln.replace("<","")
			eachSoln = eachSoln.replace(">","")
			eachSoln = eachSoln.replace("[","")
			eachSoln = eachSoln.replace("]","")
			#print eachSoln
			score = os.popen("java -jar RTED_v1.1.jar -t"+" "+studentSoln+" "+eachSoln, "r")
			#print score.read()
			scoresOrder.append(float(score.read().rstrip()))
		print scoresOrder
		print min(scoresOrder)
		return scoresOrder
	def calcScoreSingle(studentSoln, correctSoln):
		studentSoln = studentSoln.replace("<","")
		studentSoln = studentSoln.replace(">","")
		studentSoln = studentSoln.replace("[","")
		studentSoln = studentSoln.replace("]","")
		correctSoln = correctSoln.replace("<","")
		correctSoln = correctSoln.replace(">","")
		correctSoln = correctSoln.replace("[","")
		correctSoln = correctSoln.replace("]","")
		score = os.popen("java -jar RTED_v1.1.jar -t"+" "+studentSoln+" "+correctSoln, "r")
		#print score.read()
		return score.read().rstrip()
		

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
		#print "DATA "+tree
		#print treeList
		
	#print treeList
	
	for item in treeList:
		treeData = item.split(',')
		if(len(treeData) == 3):
			levelNum = treeData[0]
			timestamp = treeData[1]
			treeStructure = treeData[2]
			#print "Level1 "+str(timestamp)
			if(levelNum == 'Level 1'):
				level1List.append(timestamp+","+treeStructure)
			elif(levelNum == 'Level2'):
				level2List.append(timestamp+","+treeStructure)
		
	#print level1List[len(level1List)-1].split(",")[0]
	#init_scores = calcScore(level1List[len(level1List)-1].split(",")[1], solutionsListForLevel1)
	#print min(init_scores)	
	#leastScoreIndex = init_scores.index(min(init_scores))
	#print min(init_scores)
	for item in level1List:
		global firstTime
		treeData = item.split(',')
		timestamp = treeData[0]
		treeStructure = treeData[1]
		#with open(tempFile, 'w') as temp:
		#temp.write(treeStructure)
		#print 'Level1'
		#treeScores1 = calcScore(treeStructure, solutionsListForLevel1)
		treeScores = calcScore(treeStructure, solutionsListForLevel1)
		print treeScores
		#print timestamp+":"+str(treeScore)
		#print "Initial "+str(timestamp)
		if(min(treeScores) == 0.0):
			firstTime = 1
			csvwrite(timestamp, min(treeScores))
			break
		else:
			csvwrite(timestamp, min(treeScores))
			
	'''
	if(len(level2List)>0):
		init_scores = calcScore(level2List[len(level2List)-1].split(",")[1], solutionsListForLevel2)
		#print min(init_scores)	
		leastScoreIndex = init_scores.index(min(init_scores))
		#print min(init_scores)
		for item in level2List:
			global firstTime
			treeData = item.split(',')
			timestamp = treeData[0]
			treeStructure = treeData[1]
			#with open(tempFile, 'w') as temp:
			#temp.write(treeStructure)
			#print 'Level1'
			#treeScores1 = calcScore(treeStructure, solutionsListForLevel1)
			treeScores = calcScoreSingle(treeStructure, solutionsListForLevel2[leastScoreIndex])
			#print timestamp+":"+str(treeScore)
			#print "Initial "+str(timestamp)
			if(float(treeScores) == 0.0):
				firstTime = 1
				csvwrite(timestamp, treeScores)
				break
			else:
				csvwrite(timestamp, treeScores)
	'''
