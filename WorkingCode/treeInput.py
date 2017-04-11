import os

inputTree = ''
bracketCount = 0


def parseOpcodeInput(inputFile, outputFile):
	#the opcodes file
	fileRead = open(inputFile,'r')
	inpOpcodes = fileRead.readlines()
	global inputTree
	global bracketCount
	for i in range(len(inpOpcodes)):
		if(i != len(inpOpcodes)-1):
			inputTree+= '{'+inpOpcodes[i].rstrip()
			bracketCount+= 1
		else:
			inputTree+= '}'*bracketCount

	#the java jar format input file
	fileWrite = open(outputFile,'w')
	fileWrite.write(inputTree)
	print 'File written!'


def calcScore(file1, file2):
	#include the input tree data files
	#file1 = "/home/vanrao/Desktop/InputsForEditDist.txt"
	#file2 = "/home/vanrao/Desktop/InputsForEditDist2.txt"
	os.system("java -jar RTED_v1.1.jar -f"+" "+file1+" "+file2+" "+"-s left")


#parseOpcodeInput('sampleInp.txt', 'InputsForEditDist2.txt')
#parseOpcodeInput('sampleInp2.txt', 'InputsForEditDist.txt')

calcScore('InputsForEditDist.txt', 'InputsForEditDist2.txt')
