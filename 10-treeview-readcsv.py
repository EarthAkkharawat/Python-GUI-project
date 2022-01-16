from tkinter import*
from tkinter import ttk
from tkinter import simpledialog
from datetime import datetime
import csv

def Writetocsv(ep):
	with open('treeview.csv', 'a', newline ='', encoding = 'utf-8') as file:
		# 'a' = append , 'w' = replace
		fw = csv.writer(file)#fw is filewriter
		#ep = ['cat', 800]
		fw.writerow(ep)
	
	print('Done!')

def Readcsv():
	with open('treeview.csv', newline='', encoding = 'utf-8') as file:
		#fr = filereader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data


GUI = Tk() #This is the main window of program.
GUI.title('Example')

w = 700
h = 500


ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws, hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #Adjust the box size.

header = ['Date-time', 'List', 'Cost']

table_expense = ttk.Treeview(GUI, column = header, show = 'headings', height = 20)
table_expense.pack()

table_expense.heading('Date-time', text = 'Date-time')
table_expense.heading('List', text = 'List')
table_expense.heading('Cost', text = 'Cost')

def AddList(event = None):
	ep = simpledialog.askstring('Fill in the blank', 'Saving lists', parent = GUI)
	price = simpledialog.askstring('Fill in the blank', 'Amount of money', parent = GUI)
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #Can visit strftime.org website.
	data = [dt, ep, price] #input information.
	print('DATA:', data)
	if ep != None and price != None and len(ep) != 0 and len(price) != 0: # != is not equal.
		table_expense.insert('', 'end', value = data) #fill values in the table according to the above information.
		Writetocsv(data)
	elif ep != None and (price == None and len(ep) != 0):
		data = [dt, ep, '-']
		table_expense.insert('', 'end', value = data)
		Writetocsv(data)
	else:
		pass



GUI.bind('<F1>', AddList) #GUI.bind('<button name>', function name) must input "event = None" in function.

B1 = ttk.Button(GUI, text = 'Adding list', command = AddList)
B1.pack(pady = 10, ipadx = 20, ipady = 10)


def update_table():
	data = Readcsv()
	print(data)
	for dt in data:
		table_expense.insert('', 'end', value = dt)



update_table()







GUI.mainloop()#This input makes the program run all the time.
