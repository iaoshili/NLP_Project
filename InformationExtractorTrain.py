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
fileNameForChecking = "fileForChecking"

'''
Build a list of words.
Such that all the sentences containing labeled deadlines will put all their componenet words inside this list.
For stanford, only need to care about DATE and LOCATION
Other keys include "Sentences" and I series
'''
wordsFromSentencesContainingDeadlines = []
stopwordList = stopwords.words('english')
stopwordList += string.punctuation


def getDeadline(data):
	if data.has_key("Ideadline") == False:
		return
	else:
		if data.has_key("DATE") == False:
			return
		sentences = data["Sentences"]
		dates = data["DATE"]
		deadline = set()
		for sentence in sentences:
			if "deadline" in sentence.lower() in sentence.lower() or "due" in sentence.lower():
				for date in dates:
					if date.lower() in sentence.lower():
						if formatter(date) != "Not Provided":
							deadline.add(formatter(date))
		return ' '.join(deadline)

def getToeflRequirement(data):
	if data.has_key("Itoefl") == False:
		return
	else:
		sentences = data["Sentences"]
		toeflRequiement = set()
		for sentence in sentences:
			potentialField = [int(s) for s in sentence.split() if s.isdigit()]

			ignoreThisSentence = False
			if data.has_key("DATE"):
				for date in data["DATE"]:
					if date.lower() in sentence.lower():
						ignoreThisSentence = True
			if ignoreThisSentence:
				continue

			if "toefl" in sentence.lower() or "test" in sentence.lower():
				for num in potentialField:
					if 80 <= num <= 120 or 10 <= num <= 25:
						toeflRequiement.add(str(num))
		return ' '.join(toeflRequiement)

def getToeflCodeRequirement(data):
	if data.has_key("Itoeflcode") == False:
		return
	else:
		sentences = data["Sentences"]
		toeflRequiement = set()
		for sentence in sentences:
			potentialField = [int(s) for s in sentence.split() if s.isdigit()]

			ignoreThisSentence = False
			if data.has_key("DATE"):
				for date in data["DATE"]:
					if date.lower() in sentence.lower():
						ignoreThisSentence = True
			if ignoreThisSentence:
				continue

			if "code" in sentence.lower() in sentence.lower():
				for num in potentialField:
					toeflRequiement.add(str(num))
		return ' '.join(toeflRequiement)

def saveToLocal(data):
	fileName = "toeflcode"
	saveDirectory = os.getcwd()+"/"+"ForChecking/"
	filePath = saveDirectory + fileName

	output = ""
	for collegeName in collegeInformations.keys():
		data = collegeInformations[collegeName]
		instance = ""
		Gcontent = ""
		Icontent = ""
		Gfield = "G"+fileName
		Ifield = "I" + fileName
		if data[Gfield] != None:
			Gcontent = data[Gfield].encode("utf-8")
		if data.has_key(Ifield):
			Icontent = " ".join(data[Ifield]).encode("utf-8")
		instance += "The collegeName is: "+collegeName+"\n"
		instance += "The " + fileName + " we estimate is: "+Gcontent+"\n"
		instance += "The true " + fileName +" is: "+Icontent+"\n"+"\n"
		output += instance

	f = open(filePath,'w')
	f.write(output)
	f.close()  


collegeInformations = {}
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

		collegeInformations[fileNames[i]] = data

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

# if "deadline" in collegeInformations["University of Wisconsin—​Madison "]["Sentences"][6]
for collegeName in collegeInformations.keys():
	# if "columbia".lower() in collegeName.lower():
	collegeInformations[collegeName]["Gdeadline"] = getDeadline(collegeInformations[collegeName])
	collegeInformations[collegeName]["Gtoefl"] = getToeflRequirement(collegeInformations[collegeName])
	collegeInformations[collegeName]["Gtoeflcode"] = getToeflCodeRequirement(collegeInformations[collegeName])


saveToLocal(collegeInformations)

# deadline_words = nltk.FreqDist(w.lower() for w in wordsFromSentencesContainingDeadlines)
# sorted_freqDeadlineWordsDict = sorted(deadline_words.items(), key=operator.itemgetter(1), reverse = False)
# for wordAndOccurence in sorted_freqDeadlineWordsDict:
# 	print "The occurence of %s is %d" % (wordAndOccurence[0].encode("utf-8"), wordAndOccurence[1])

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
