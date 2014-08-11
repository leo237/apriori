#Abhilash Panigrahi

#Importing modules
import nltk
from nltk.tag.simplify import simplify_wsj_tag
import csv

#defining useless words that might crop into data.
useless = ["is", "was", "been", "have", "had", "(", ")"]

#Function to segregate based on Parts of speech. 
def check(id,pos):
	if (pos[1] == "N" or pos[1] == "NP" or pos[1] == "V" or pos[1] == "VD" or pos[1] == "VN" or pos[1] == "ADJ") and (pos[0] not in added): #Too long. Should consider making a list and then checking if its there in it
		e = []
		e.append(id)
		e.append(pos[0])
		collection.append(e)
		added.append(pos[0])

#Implementation starts here. Reads file for input.
f = open('input.txt')
lines = f.readlines()
f.close
count = 0

#Creating empty lists.
collection = []
header = ["Setence ID", "Word"]
collection.append(header)

#For every line read in the file. 
for line in lines:

	added = []
	tokens = nltk.word_tokenize(line)  #Tokenizing by word.
	tagged = nltk.pos_tag(tokens)

	simplified = [(word, simplify_wsj_tag(tag)) for word, tag in tagged] #To create simplified POS tags.
	print simplified
	num = len(simplified)

	for i in xrange(num):
		# print simplified[i][0] ,   #Testing purpose.
		# print simplified[i][1]
		if simplified[i][0] not in useless:
			check(count,simplified[i]) #Function call
	count = count + 1	



with open('finalTable3.csv','wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for eachList in collection:
		wr.writerow(eachList)

