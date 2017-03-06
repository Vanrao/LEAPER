from sklearn.feature_extraction.text import Tfidfvectorizer
from sklearn.cluster import KMeans
import numpy as np
import csv

# TODO : Read data from the csv
documents=[]
with open() as csvfile:
	inputData=csv.reader(csvfile,delimiter=" ")
	for rows in inputData:
		

#Remove all stopwords since all characters are taken
vectorizer=Tfidfvectorizer(stop_words=None)
Train_X=vectorizer.fit_transform(documents)

num_Of_clusters=3
model= KMeans(n_clusters=num_Of_clusters,init='k_means++',max_iter=100,n_init=1)
model.fit(Train_X)

labels=model.labels_
order_centroids=model.cluster_centers_.argsort()[:, ::-1]

#Predict the test label for new data.
testLabels=model.predict(newTestData)
