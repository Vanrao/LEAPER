import csv 
import pickle
import os
import numpy as np
from sklearn.cluster import KMeans

csvdict = {}
newDict = {}
newList = []
filenames = []
prev = 0
csvfile = open("./Level_1_Scores/9-j-8538.csv","r")
prefix = "/home/vanrao/Trialdata/Level_1_Scores/"
pickledFiles = "/home/vanrao/Trialdata/PickledFiles/"
MAX_TIMESTAMP = 782871

'''for files in os.listdir("/home/vanrao/Trialdata/Level_1_Scores/"):
	print prefix+files
	fileCsv = open(prefix+files,"r")
	csvreader = csv.reader(fileCsv, delimiter=",")
	for rows in csvreader:
		csvdict.update({float(rows[0]):float(rows[1])})

	print len(csvdict)

	#MAX_TIMESTAMP = 160569692
	
	#writeCsv = open("Temp.csv", "w")
	#csvwriter = csv.writer(writeCsv, delimiter = ",")

	for i in range(0, MAX_TIMESTAMP+1):
		#print i
		if(i in csvdict.keys()):
			#csvwriter.writerow([i, csvdict[i]])
			newDict.update({i:csvdict[i]})
			prev = csvdict[i]
		else:
			#csvwriter.writerow([i, prev])
			newDict.update({i:prev})
	fileName = files.replace(".csv", "")
	with open(pickledFiles+fileName+'.pickle', 'wb') as handle:
		pickle.dump(newDict, handle, protocol = pickle.HIGHEST_PROTOCOL)
	#break
	csvdict = {}
	#print newDict'''

for pck in os.listdir(pickledFiles):
	filenames.append(pck)
	handle = open(pickledFiles+pck, 'rb')
	dictionary = pickle.load(handle)
	newList.append(dictionary.values())

trainData = np.array(newList)
#TestData = np.array()

num_Of_clusters = 2
model = KMeans(n_clusters = num_Of_clusters,init = 'random',max_iter = 1000,n_init = 2)
model.fit_transform(trainData)
print model.labels_
for i,j in zip(filenames, model.labels_):
	print i+" : "+str(j)
	
#model.tranform(TestData)

