import csv
with open('finalTable.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print row[0]