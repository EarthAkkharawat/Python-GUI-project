import csv

def Readcsv():
	with open('treeview.csv', newline='', encoding = 'utf-8') as file:
		#fr = filereader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data

expense = Readcsv()
print(expense[0][0])