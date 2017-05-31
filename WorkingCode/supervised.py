import csv 
import pickle
import os
import numpy as np
from sklearn.cluster import KMeans
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn import tree

csvdict = {}
newDict = {}
newList = []
filenames = []
taglables = []
prev = 0
csvfile = open("./Level_1_Scores/9-j-8538.csv","r")
prefix = "/home/vanrao/Trialdata/Level_1_Scores/"
pickledFiles = "/home/vanrao/Trialdata/PickledFiles/"
MAX_TIMESTAMP = 782871

with open("/home/vanrao/Trialdata/TaggedTrained.csv", "r") as op:
	csvrdr = csv.reader(op, delimiter = ",")
	for rows in csvrdr:
		handle = open(rows[0], 'rb')
		dictionary = pickle.load(handle)
		newList.append(dictionary.values())
		taglables.append(rows[1])
	trainData = np.array(newList)
	tagstrained = np.array(taglables)
#TestData = np.array()
train = trainData[0:35]
test = trainData[36:]

#clf=MultinomialNB()	
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train, tagstrained[0:35])

print accuracy_score(tagstrained[36:],clf.predict(test))
'''num_Of_clusters = 2
model = KMeans(n_clusters = num_Of_clusters,init = 'random',max_iter = 1000,n_init = 2)
model.fit_transform(trainData)
print model.labels_
for i,j in zip(filenames, model.labels_):
	print i+" : "+str(j)
	
#model.tranform(TestData)'''

