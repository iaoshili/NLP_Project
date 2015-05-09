import collections, itertools
from nltk import metrics
from nltk.classify import util, ClassifierI, MultiClassifierI
from nltk.probability import FreqDist

def precision_recall_fmeasure(classifier, testfeats, tag):
	trueTagDocs = 0
	mytagDocs = 0
	mytagAndTrueDocs = 0

	for feature,label in testfeats:
		if label == tag:
			trueTagDocs += 1
		if classifier.classify(feature) == tag:
			mytagDocs += 1
			if label == tag:
				mytagAndTrueDocs += 1

	precision = float (mytagAndTrueDocs)/mytagDocs
	recall = float (mytagAndTrueDocs)/trueTagDocs
	fmeasure = 2*precision*recall/(precision+recall)
	return precision, recall, fmeasure