from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.mixture import GMM
from sklearn.neural_network import BernoulliRBM
from collections import Counter
import numpy as np
import csv
import operator
import os


# TODO : Read data from the csv
documents=[]
count=0
prevTime=0
currData=[0,0]
headerList=["sensing_touchingobjectmenu","sensing_touchingobject","sensing_keypressed","sensing_keyoptions","motion_pointindirection","motion_movesteps","motion_gotoxy","math_number","math_angle","looks_switchbackdropto","looks_show","looks_backdrops","event_whenflagclicked","event_whenbackdropswitchesto","control_if","control_forever"]
#print len(headerList)
valList=[]
timestampDict={}
copy={}
keyset=[]
Train_X=[]
tempList=[]

def createStudentInput(inputData,wrtdata,fileRead):
	for rows in inputData:
		print fileRead
		timestamp=int(rows[0])
		#print timestamp
		opcode=rows[2]
		valList.append([timestamp,opcode])

	for items in valList:
		if(items[0] in timestampDict):
			timestampDict[items[0]].append(items[1])
		else:
			timestampDict[items[0]]=[]
			timestampDict[items[0]].append(items[1])

	diffList=[0]
	keyset=timestampDict.keys()
	for i,j in zip(range(0,len(keyset)),range(1,len(keyset))):
		diff=keyset[j]-keyset[i]
		diffList.append(diff)
	#print len(diffList)
	i=0
	for k,v in timestampDict.items():
		freq=Counter(v)
		wrtdata.writerow([k,freq[headerList[0]],freq[headerList[1]],freq[headerList[2]],freq[headerList[3]],freq[headerList[4]],freq[headerList[5]],freq[headerList[6]],freq[headerList[7]],freq[headerList[8]],freq[headerList[9]],freq[headerList[10]],freq[headerList[11]],freq[headerList[12]],freq[headerList[13]],freq[headerList[14]],freq[headerList[15]],diffList[i]])
		i+=1

	#wtrfile.close()
		


def createInputCsv():
	outerDir="/home/vanrao/scratch-vm/LEAPER-master/Scratch_Workshop/"
	for dirs in os.listdir(outerDir):
		num=0
		for eachDir in os.listdir(outerDir+dirs):
			fileName=outerDir+dirs+"/"+eachDir
			fileReader=open(fileName,'r')
			dataInput=csv.reader(fileReader,delimiter=" ")
			num+=1
			wtrfile=open(outerDir+dirs+"/"+"Text"+str(num)+".csv",'w+')
			dataWrite=csv.writer(wtrfile,delimiter=",")
			try:
				createStudentInput(dataInput,dataWrite,fileName)
			except:
				pass


# CSV headers are timestamp,headerList,time difference

def readCsvData():
	outerDir="/home/vanrao/scratch-vm/LEAPER-master/Scratch_Workshop/"
	for dirs in os.listdir(outerDir):
		for eachDir in os.listdir(outerDir+dirs):
			if "Text" in str(eachDir):
				#tempList=[]
				fileName=outerDir+dirs+"/"+eachDir
				fileReader=open(fileName,'r')
				dataInput=csv.reader(fileReader,delimiter=",")
				for lines in dataInput:
					for items in lines:
						tempList.append(float(items))
				Train_X.append(tempList)
	



readCsvData()
#print Train_X[0]
#print final	
Test_X=Train_X[:15]
Test_Y=Train_X[15:]
print len(Test_X)
#print Train_X
#Remove all stopwords since all characters are taken
#vectorizer=Tfidfvectorizer(stop_words=None)
#Train_X=vectorizer.fit_transform(documents)
X=np.array(Test_X)
#print type(X)
#print Train_X
"""num_Of_clusters=3
model= KMeans(n_clusters=num_Of_clusters,init='random',max_iter=1000,n_init=2)
model.fit_transform(X)
labels=model.labels_
order_centroids=model.cluster_centers_.argsort()[:, ::-1]"""


"""model=GMM(n_components=2)
model.fit(X)"""

model=BernoulliRBM(n_components=2)
model.fit(X)

#Predict the test label for new data.
testLabels=model.transform(Test_Y)

print testLabels
