# -*- coding: utf-8 -*-

from nltk.corpus import movie_reviews
import nltk
import random
import json
from pprint import pprint
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import WordPunctTokenizer
import os
import codecs
import operator
import string
import pickle
# from featx import label_feats_from_corpus, split_label_feats
# from featx import bag_of_words
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.classify.util import accuracy
from classification import precision_recall_fmeasure
from sklearn import svm
from sklearn.svm import NuSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from featx import high_information_words
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
from tagRecommender import *

dataDirectory = "/Users/Greyjoy/Documents/Homework/NLP_Project/Data/AI_News/"


def getCleanStructuredData(data, quality):
	#Deal with text
	# stopwordList = stopwords.words('english')
	# stopwordList += string.punctuation

	# tokens = WordPunctTokenizer().tokenize(data)
	# stemmer = nltk.PorterStemmer()
	# tokens = [stemmer.stem(t).lower() for t in tokens]
	# tokens = [x for x in tokens if ((x in stopwordList) == False)]

	cleanedData = []
	cleanedData.append(data)
	cleanedData.append(quality)
	return cleanedData
		
def extractWordFeatureSet(cleanedDataCollection):
	wordList = []
	for data in cleanedDataCollection:
		text = data[0]
		wordList += text
	#Get a dictionary. Key is a word, value is how many time it occurs in the corpus
	all_words = nltk.FreqDist(w.lower() for w in wordList)
	#Sort the words in the order of their frequency. From high to low.
	sorted_freqWords = sorted(all_words.items(), key=operator.itemgetter(1), reverse = True)
	word_features = []
	for i in xrange(0,NUM_FEATUREWORDS):
		word_features.append(sorted_freqWords[i][0])
	return word_features

def extractFeatures(document, tagPool):
	features = {}
	for word,numDocs in tagPool:
		features[word] = 0.0

	recommendTags = coreTags(document)
	for tag,score in recommendTags:
		if (tag in features.keys()) == False:
			continue
		else:
			features[tag] = score
	return features


def train(cleanedDataCollection, tagPool):
	posSamples = []
	negSamples = []

	featuresets = [(extractFeatures(d,tagPool), c) for (d,c) in cleanedDataCollection]
	for sample in featuresets:
		if sample[1] == "trash":
			negSamples.append(sample)
		else:
			posSamples.append(sample)

	train_set = negSamples[10:]+posSamples[10:]
	test_set = negSamples[:10]+posSamples[:10]


	# classifier = nltk.NaiveBayesClassifier.train(train_set)
	# print(nltk.classify.accuracy(classifier, test_set))
	# classifier.show_most_informative_features(5) 
	# return classifier

	sk_classifier = SklearnClassifier(MultinomialNB())
	sk_classifier.train(train_set)
	print "accuracy is: %s" % (accuracy(sk_classifier, test_set))

	precision, recall, fMeasure = precision_recall_fmeasure(sk_classifier,  test_set, "useful")

	print "precision is: %s" % (precision)
	print "recall is: %s" % (recall)
	print "F-measure is: %s" % (fMeasure)
	return sk_classifier



cleanedDataCollection = []
for fileName in os.listdir(dataDirectory):
	filePath = dataDirectory + fileName
	with open(filePath) as data_file: 	
		input_file  = file(filePath, "r")
		data = input_file.read()
		data = data.decode('utf-8',errors='ignore')
		if "trash" in fileName:
			cleanedData = getCleanStructuredData(data, "trash")
		else:
			cleanedData = getCleanStructuredData(data, "useful")
		cleanedDataCollection.append(cleanedData)

tagPool = getTagSet()
classifier = train(cleanedDataCollection, tagPool)

currDir = os.getcwd()
f = open(currDir+"/"+'interestingArticleIdentifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()