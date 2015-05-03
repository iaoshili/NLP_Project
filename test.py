import nltk


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

def getEntity(sentence, category):
	tokens = nltk.word_tokenize(sentence)
	pos_tags = nltk.pos_tag(tokens)
	taggedSent = nltk.ne_chunk(pos_tags, binary=False)
	print taggedSent
	namedEntities = []
	for n in taggedSent:
		try:
			n.label()
		except AttributeError:
			#Do nothing
			continue
		else:
			if n.label() == category:
				entity = ""
				for nameAndPOSTag in n.leaves():
					entity += nameAndPOSTag[0]+" "
				namedEntities.append(entity)
	return namedEntities

def getDeadLine(sentence):
	pass

sent = nltk.corpus.treebank.tagged_sents()[22]

if "dec" in "December".lower():
	print "yeda"
