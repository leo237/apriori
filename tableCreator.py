#Abhilash Panigrahi

#Importing modules
import nltk
from nltk.tag.simplify import simplify_wsj_tag
import csv

#defining useless words that might crop into data.
useless = ["is", "was", "been", "have", "had", "(", ")"]

#Function to segregate based on Parts of speech. 
def check(id,pos):
	if pos[1] == "N" or pos[1] == "NP":
		noun[id].append(pos[0])
	
	elif pos[1] == "V" or pos[1] == "VD" or pos[1] == "VN":
		verb[id].append(pos[0])
		
	elif pos[1] == "ADJ":
		adjective[id].append(pos[0])
		
#Implementation starts here. Reads file for input.
f = open('input.txt')
lines = f.readlines()
f.close
count = 0

#Creating empty lists.
noun = []
verb = []
adjective = []

#For every line read in the file. 
for line in lines:
	c = []	 #An empty list that will be added to the main list. 2d List.
	d = []
	e = []
	noun.append(c)
	verb.append(d)
	adjective.append(e)

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

#For sentences without any specific POS, we are appending NA to the list corresponding to the sentence. 
for li in noun:
	if (len(li) == 0):
		li.append("NA")

for li in verb:
	if (len(li) == 0):
		li.append("NA")

for li in adjective:
	if (len(li) == 0):
		li.append("NA")

#Printing the data on the screen.
print "noun:"	
for a in noun:
	print a,
print "\n"

print "verb:"
for b in verb:
	print b,
print "\n"

print "adjective"
for c in adjective:
	print c,

print "\nFinal List"


#Create a final list with noun,verb and adjective collected together.
finalList = []
header = ["Setence ID", "Noun", "Verb", "Adjective"]
finalList.append(header)

i =1
while(i<=len(lines)):
	temp = []
	finalList.append(temp)
	k = i
	k = int(k)
	finalList[i].append(k)
	finalList[i].append(noun[i-1])
	finalList[i].append(verb[i-1])
	finalList[i].append(adjective[i-1])
	i = i+1

#print finalList

#Create a csv from the above list

with open('finalTable.csv','wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	for eachList in finalList:
		wr.writerow(eachList)

