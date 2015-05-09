from keyWordExtraction import RakeKeywordExtractor
from nltk.corpus import wordnet as wn
import sys
import codecs
#print all the synset element of an element
def lemmalist(word):
    syn_set = []
    for synset in wn.synsets(word):
        for item in synset.lemmas():
            syn_set.append(item.name())
    return syn_set


def getTagSet():
	f = codecs.open("raw_tags", encoding='utf-8')
	lines = f.read()
	f.close()
	lines = lines.split("\n")
	tags = []
	for line in lines:
		if len(line.split()) == 0:
			continue
		rawTag = line.split()[:-2]
		tagPopularity = line.split()[-2].encode('utf-8')
		tagPopularity = int (tagPopularity.replace(',', ''))
		tag = " ".join(rawTag)
		tags.append([tag.lower(),tagPopularity])
	return tags


def keywords(text):
	rake = RakeKeywordExtractor()
	keywords = rake.extract(text, incl_scores=True)
	return keywords

def coreTags(text):
	coreTags = []

	tags = getTagSet()
	rake = RakeKeywordExtractor()
	keywords = rake.extract(text, incl_scores=True)
	tagsInArticles = set()
	for keyword in keywords:
		tagsInArticles.add(keyword)
	for keyword,score in tagsInArticles:
		for tag,tagPopularity in tags:
			if (tag.lower() == keyword.lower()):
				coreTags.append([tag, tagPopularity*score])
	coreTags = sorted(coreTags, key=lambda x: x[1], reverse=True)
	return coreTags


def additionalTags(text):
	additionalTags = []
	tags = getTagSet()
	rake = RakeKeywordExtractor()
	keywords = rake.extract(text, incl_scores=True)
	similarWordDict = {}
	tagsInArticles = set()

	for keyword,score in keywords:
		if len(keyword.split()) > 1:
			continue
		tagsInArticles.add(keyword)
		similarWords = lemmalist(keyword)
		if len(similarWords) != 0:
			for word in similarWords:
				if ((word in tagsInArticles) == False):
					similarWordDict[word] = score

	for keyword in similarWordDict.keys():
		for tag,tagPopularity in tags:
			if (tag.lower() == keyword.lower()):
				additionalTags.append([tag, tagPopularity*similarWordDict[keyword]])
	additionalTags = sorted(additionalTags, key=lambda x: x[1], reverse=True)
	return additionalTags[:20]


#Demo
# f = codecs.open("testFile", encoding='utf-8')
# content = f.read()
# f.close()
# print keywords(content)
# print coreTags(content)
# print additionalTags(content)
