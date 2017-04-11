import os
import csv

# can only be written into files
#global tree
tree = ''
treeList = []
studentScores = 'studentTreeScores.csv'

#tree format input text file of student block data
fileName = 'treeOutput_1.txt'
tempFile = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/temp.txt'

#correct soln-No.1
corSoln = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/ttt.txt'

#for solution 1
ff = open(studentScores, 'w')
def csvwrite(timestamp, score):
	csvwriter = csv.writer(ff, delimiter=',')
	csvwriter.writerow([timestamp,float(score)])


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def calcScore(studentSoln):
	score = os.popen("java -jar RTED_v1.1.jar -f"+" "+studentSoln+" "+corSoln+" "+"-s left", "r")
	return score.read()

with open(fileName,'r') as f:
	data = f.read().splitlines()
#print data
for eachData in data:
	if(eachData != ''):
		if(isInt(eachData)):
			tree = tree + eachData+','
		else:
			tree = tree + eachData
	else:
		treeList.append(tree)
		tree = ''

#print treeList
for item in treeList:
	treeData = item.split(',')
	timestamp = treeData[0]
	treeStructure = treeData[1]
	with open(tempFile, 'w') as temp:
		temp.write(treeStructure)
	treeScore = calcScore(tempFile)
	#print timestamp+":"+str(treeScore)
	csvwrite(timestamp, treeScore)
	open(tempFile, 'w').close()
	#print "\n"

