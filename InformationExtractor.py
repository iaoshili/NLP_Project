# -*- coding: utf-8 -*-
import random
import json
from pprint import pprint
import os
import codecs
import nltk
import random
import json
from pprint import pprint
from nltk import word_tokenize
import os
import codecs
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import WordPunctTokenizer
import operator
import yaml
from nltk.stem.snowball import SnowballStemmer
import string
from formatter import *

workingDirectory = "/Users/Greyjoy/Documents/Homework/NLP_Project/Data/BeautifulData/"

'''
Build a list of words.
Such that all the sentences containing labeled deadlines will put all their componenet words inside this list.
'''
wordsFromSentencesContainingDeadlines = []
stopwordList = stopwords.words('english')
stopwordList += string.punctuation

def getCleanStructuredData(text):
	#Deal with text
	stopwordList = stopwords.words('english')
	stopwordList += string.punctuation

	tokens = WordPunctTokenizer().tokenize(text)
	stemmer = nltk.PorterStemmer()
	tokens = [stemmer.stem(t).lower() for t in tokens]
	tokens = [x for x in tokens if ((x in stopwordList) == False)]

	cleanedData = tokens
	return cleanedData

def getDeadline(sentence):
	

print getCleanStructuredData("deadlines")

# fileNames = os.listdir(workingDirectory)
# for i in xrange(0,len(fileNames)-1):
# 	filePath = workingDirectory + fileNames[i]
# 	# print filePath
# 	# print "%s\'s university start" % (i)
# 	with open(filePath) as data_file:
# 		if "DS_Store" in filePath:
# 		 	continue
# 		# data = json.load(data_file)
# 		input_file  = file(filePath, "r")
# 		data = json.loads(input_file.read())
# 		# data = byteify(data)

# 		for sentence in data["Sentences"]:
# 			if data.has_key("Igre"):
# 				for Ideadline in data["Igre"]:
# 					if Ideadline in sentence:
# 						tokens = WordPunctTokenizer().tokenize(sentence)
# 						# stemer = SnowballStemmer("english")
# 						# stemer = nltk.PorterStemmer()
# 						# tokens = [stemer.stem(t).lower() for t in tokens]
# 						tokens = [x for x in tokens if ((x in stopwordList) == False)]
# 						wordsFromSentencesContainingDeadlines += tokens
# 						break

# deadline_words = nltk.FreqDist(w.lower() for w in wordsFromSentencesContainingDeadlines)
# sorted_freqDeadlineWordsDict = sorted(deadline_words.items(), key=operator.itemgetter(1), reverse = False)
# for wordAndOccurence in sorted_freqDeadlineWordsDict:
# 	print "The occurence of %s is %d" % (wordAndOccurence[0].encode("utf-8"), wordAndOccurence[1])

