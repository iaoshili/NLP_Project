from tagRecommender import *
import json
import os

dataDirectory = "/Users/Greyjoy/Documents/Homework/NLP_Project/Data/MIT_NEWS/"

right_tags_num = 0.0
true_tags_num = 0.0
my_tags_num = 0.0

for fileName in os.listdir(dataDirectory):
	filePath = dataDirectory + fileName
	if ".DS_Store" in filePath:
		continue
	with open(filePath) as data_file: 	
		news = json.load(data_file)
		my_tags = coreTags(news["content"])	
		my_tags_num += len(my_tags)
		true_tags = news["tags"]
		true_tags_num += len(true_tags)

		for tag,score in my_tags:
			for true_tag in true_tags:
				if tag.lower() == true_tag.lower():
					right_tags_num += 1
		
precision = right_tags_num/my_tags_num
recall =  right_tags_num/true_tags_num
print precision
print recall