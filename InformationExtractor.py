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

workingDirectory = "/Users/Greyjoy/Documents/Homework/NLP_Project/Data/BeautifulData/"

'''
Build a list of words.
Such that all the sentences containing labeled deadlines will put all their componenet words inside this list.
'''
wordsFromSentencesContainingDeadlines = []
stopwordList = stopwords.words('english')
stopwordList += string.punctuation


fileNames = os.listdir(workingDirectory)
for i in xrange(0,len(fileNames)-1):
	filePath = workingDirectory + fileNames[i]
	# print filePath
	# print "%s\'s university start" % (i)
	with open(filePath) as data_file:
		if "DS_Store" in filePath:
		 	continue
		# data = json.load(data_file)
		input_file  = file(filePath, "r")
		data = json.loads(input_file.read())
		# data = byteify(data)

		for sentence in data["Sentences"]:
			if data.has_key("Igre"):
				for Ideadline in data["Igre"]:
					if Ideadline in sentence:
						tokens = WordPunctTokenizer().tokenize(sentence)
						# stemer = SnowballStemmer("english")
						# stemer = nltk.PorterStemmer()
						# tokens = [stemer.stem(t).lower() for t in tokens]
						tokens = [x for x in tokens if ((x in stopwordList) == False)]
						wordsFromSentencesContainingDeadlines += tokens
						break

deadline_words = nltk.FreqDist(w.lower() for w in wordsFromSentencesContainingDeadlines)
sorted_freqDeadlineWordsDict = sorted(deadline_words.items(), key=operator.itemgetter(1), reverse = False)
for wordAndOccurence in sorted_freqDeadlineWordsDict:
	print "The occurence of %s is %d" % (wordAndOccurence[0].encode("utf-8"), wordAndOccurence[1])

# for word in all_words.keys():
# 	print word+str(all_words[word])
# print all_words.keys()

			# if "deadline" in sentence:
			# 	for potentialDeadline in data["DATE"]:
			# 		if potentialDeadline in sentence:
			# 			print potentialDeadline.encode("utf-8")
				# print sentence.encode("utf-8")

		# if "Ideadline" in data.keys():
		# 	for deadline in data["Ideadline"]:
		# 		newDeadline = deadline.encode("utf-8")
		# 		print newDeadline.translate(None, '!@#,$')
