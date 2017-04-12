import os
import getTreeEditdistScore

i=1
csvdata = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/'
level2file = '/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/lll.csv'

filePath = "/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/FinalOpcodes/"
files = os.listdir("/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/FinalOpcodes/")
for f in files:
	getTreeEditdistScore.createCsvs(csvdata+str(i)+".csv", level2file, filePath+f)
	break
	#i=i+1
	

