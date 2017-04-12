import os
import getTreeEditdistScore

i=1
csvdata = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/'


filePath = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/FinalOpcodes/"
files = os.listdir("/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/FinalOpcodes/")
for f in files:
	getTreeEditdistScore.createCsvs(csvdata+str(i)+".csv", filePath+f)
	i=i+1
	

