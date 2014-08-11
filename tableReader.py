import csv
import MySQLdb

threshholdSupport = 0.6

#Database connection takes here. 
conn = MySQLdb.connect("localhost","root", "", "researchProject")
x = conn.cursor()
x.execute("TRUNCATE TABLE research")
conn.commit()
#Apparently commit is required for everthing to actually take place. Odd...

count = 0
#I'm reading through the csv file and then inserting them into the SQL database to make life much easier. 
with open('finalTable3.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', skipinitialspace=True, quotechar='|')
	for row in spamreader:
		if count == 0:
			count = 1
			continue
		sentID = row[0][1:-1]
		sentID = int(sentID)
		word = row[1][1:-1]
		# print sentID, type(sentID)
		# print word
		x.execute("INSERT INTO research values ('',%s,%s)",(sentID,word))
		conn.commit()

#Generating the frequent item set. Apriori algorithm starts here. 

frequentItemSet = "SELECT word, COUNT(*) FROM research GROUP BY word DESC"
x.execute(frequentItemSet)
frequentItemSet = x.fetchall()

numberOfsentences = "SELECT COUNT(DISTINCT(sentenceId)) FROM research"
x.execute(numberOfsentences)
numberOfsentences = x.fetchone()
numberOfsentences = int(numberOfsentences[0])

supportDict = dict()

for item in frequentItemSet:
	supportDict[item[0]] = (float(item[1])/float(numberOfsentences))

#Python does not allow you to delete dictionary object as you are iterating through them. So I am creating a list of objects then I will delete them. 
delList = []

for each in supportDict:
	if supportDict[each] < threshholdSupport:
		delList.append(each)
#Deletion takes place here. 
for item in delList:
	del supportDict[item]

print supportDict

	