from tkinter import*
from tkinter import ttk
########CSV############################
import csv
#CSV stands for comma-seperated values.


#########################WRITETOCSV for expense########################################
def Writetocsv(ep):
	with open('allexpense.csv', 'a', newline ='', encoding = 'utf-8') as file:
		# 'a' = append , 'w' = replace
		fw = csv.writer(file)#fw is filewriter
		#ep = ['cat', 800]
		fw.writerow(ep)
	
	print('Done!')


def Readcsv():
	with open('allexpense.csv', newline='', encoding = 'utf-8') as file:
		#fr = filereader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data



#########################WRITETOCSV2 for income########################################
def Writetocsv2(ep):
	with open('allincome.csv', 'a', newline ='', encoding = 'utf-8') as file:
		# 'a' = append , 'w' = replace
		fw = csv.writer(file)#fw is filewriter
		#ep = ['cat', 800]
		fw.writerow(ep)
	
	print('Done!')


def Readcsv2():
	with open('allincome.csv', newline='', encoding = 'utf-8') as file:
		#fr = filereader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data




#######MAIN GUI####################33333
GUI = Tk() #This is the main window of program.
GUI.title('Example')


w = 700
h = 600

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws, hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #Adjust the box size.
GUI.iconbitmap('wallet.ico')

##############FONT########################################
s = ttk.Style()
s.configure('my.TButton',font=('TH Sarabun New',14,'bold'))





menubar = Menu(GUI)
GUI.config(menu = menubar)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)

filemenu.add_command(label = 'Exit - (F4)', command = GUI.quit)
GUI.bind('<F4>',lambda x = None: GUI.destroy())

#helpmenu
import webbrowser

def About():
	url = 'https://www.facebook.com'
	webbrowser.open(url)



from tkinter import messagebox as msb

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = helpmenu)
helpmenu.add_command(label = 'About', command = About)
helpmenu.add_command(label = 'Donate', command = lambda: msb.showinfo('Donate', 'Account no. : 645 587 7777\nKasikorn Bank'))

from tkinter.ttk import Notebook

Tab = Notebook(GUI)
Tab.pack(fill = BOTH, expand = 1)


T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_expense = PhotoImage(file='creditcard-icon.png')
icon_income = PhotoImage(file='money-icon.png')
icon_dashboard = PhotoImage(file='summary-icon.png')


Tab.add(T1,text='expense', image=icon_expense,compound='top')
Tab.add(T2,text='income', image=icon_income,compound='top')
Tab.add(T3,text='summary', image=icon_dashboard,compound='top')


################Expense##################################################


FONT1 = ('Angsana New', 15)
FONT2 = ('Angsana New', 20, 'bold')

# v_expense use for store value that typed by user.
v_expense = StringVar()

# E1 is a box to fill text.
L = ttk.Label(T1, text = 'Please fill in your expense').pack() #topic above E1
E1 = ttk.Entry(T1, textvariable=v_expense, font = FONT1, width = 30)
E1.pack(pady = 10)

# v_price use for store value that typed by user.
v_price = StringVar()

# E2 is a box to fill text.
L = ttk.Label(T1, text = 'Expense (baht)').pack() #topic above E2
E2 = ttk.Entry(T1, textvariable=v_price, font = FONT1, width = 30)
E2.pack(pady = 10)

# SaveExpense is function when button is clicked, this function will work.
from datetime import datetime #time

def SaveExpense(event = None):
	exp = v_expense.get()
	pc = float(v_price.get()) #transforming striing to float
	print('list: ', exp) # v_expense.get() is to pull the value to use 
	#v_result.set('You are saving list: ' + exp + ' price: '+ v_price.get() + ' baht') should not use this method
	v_result.set(f'Saving your lists : {exp} price : {pc:,.2f} baht') #should use this format method.

	dt = datetime.now().strftime('%y-%m-%d %H:%M:%S')

	data = [dt, exp, pc] #arrange information before saving in CSV.
	Writetocsv(data) #call saving function.

	#reset variables
	v_expense.set('')
	v_price.set('')
	#make cursor automatically moves to E1 box.
	E1.focus()
	update_table()

	
E2.bind('<Return>',SaveExpense) #if using "bind", it have to input "event = none" in function

# B1 is a save button.
B1 = ttk.Button(T1, text = 'Save', command = SaveExpense, style='my.TButton')
B1.pack(ipadx=20,ipady=10)

#######LABEL############
v_result = StringVar()
R1 = ttk.Label(T1, textvariable = v_result, font = FONT2, foreground = 'green')
R1.pack(pady = 20)



###########EXPENSE BUTTON############################33
expenselist = {'fried_chicken':{'name':'ไก่ทอด','price':40}
			   ,'coffee':{'name':'กาเเฟ','price':50},
			   'Taxi':{'name':'เเท็กซี่','price':100}}


########### Function ############################################

def Expense(keyword):
	price = expenselist[keyword]['price']
	print('Expenditure: ' + expenselist[keyword]['name'])
	print('Cost: ' ,price)

	ep = expenselist[keyword]['name']
	
	v_expense.set(ep)
	v_price.set(price)

########### ROW1 ##############################################

F1 = Frame(T1)# F1 is a frame
F1.pack()
# .place is for specify the position.

B1 = ttk.Button(F1, text = 'fried_chicken', command = lambda x= 'fried_chicken': Expense(x)) 
B1.grid(row = 0, column = 0, ipadx = 20, ipady = 10, padx = 5)

B2 = ttk.Button(F1, text = 'coffee', command = lambda x= 'coffee': Expense(x))
B2.grid(row = 0, column = 1, ipadx = 20, ipady = 10, padx = 5)

B3 = ttk.Button(F1, text = 'Taxi', command = lambda x= 'Taxi': Expense(x))#This button attach to F1.
B3.grid(row = 0, column = 2, ipadx = 20, ipady = 10, padx = 5)



################TABLE#############################################

header = ['Date-time', 'List', 'Cost']

table_expense = ttk.Treeview(T1, column = header, show = 'headings', height = 20)
table_expense.pack(pady = 20)

table_expense.heading('Date-time', text = 'Date-time')
table_expense.heading('List', text = 'List')
table_expense.heading('Cost', text = 'Cost')

def sum_table():
	allsum = []
	data = Readcsv()
	for dt in data:
		allsum.append(float(dt[2]))
	v_allexpense.set('{:,.2f} baht'.format(sum(allsum)))


def update_table():
	data = Readcsv()
	print(data)
	table_expense.delete(*table_expense.get_children()) #clear all the information in the table before inserting.
	for dt in data:
		table_expense.insert('', 'end', value = dt)
	sum_table()

def update_table2():
	data = Readcsv2()
	print(data)
	table_income.delete(*table_income.get_children()) #clear all the information in the table before inserting.
	for dt in data:
		table_income.insert('', 'end', value = dt)
	

################################TAB2##########################3333
v_income = StringVar()  #Store liasts of income
L = ttk.Label(T2, text = 'Please fill in income (baht)').pack() #topic above E2
E21 = ttk.Entry(T2, textvariable=v_income, font = FONT1, width = 30)
E21.pack(pady = 10)

v_incomequan = StringVar()  #store amount of income money.
L = ttk.Label(T2, text = 'Income (baht)').pack() #topic above E2
E2 = ttk.Entry(T2, textvariable=v_incomequan, font = FONT1, width = 30)
E2.pack(pady = 10)

def SaveIncome():
	print('Save income')
	incm = v_income.get()
	incmq = float(v_incomequan.get())
	print('Lists: ', incm)
	print('Amount of money: ', incmq)
	print('-----------------------')

	v_result2.set(f'Saving your lists : {incm} price : {incmq:,.2f} baht') #should use this format method.

	dt = datetime.now().strftime('%y-%m-%d %H:%M:%S')

	data = [dt, incm, incmq] #arrange information before saving in CSV.
	Writetocsv(data) #call saving function.

	#reset variables
	v_income.set('')
	v_incomequan.set('')
	#make cursor automatically moves to E1 box.
	E21.focus()
	update_table2()


B21 = ttk.Button(T2, text = 'Save', command = SaveIncome, style='my.TButton')
B21.pack(ipadx=20,ipady=10)


v_result2 = StringVar()
R2 = ttk.Label(T2, textvariable = v_result, font = FONT2, foreground = 'green')
R2.pack(pady = 20)



header = ['Date-time', 'List', 'Cost']

table_income = ttk.Treeview(T2, column = header, show = 'headings', height = 7)
table_income.pack(pady = 20)

table_income.heading('Date-time', text = 'Date-time')
table_income.heading('List', text = 'List')
table_income.heading('Cost', text = 'Cost')


###########TAB3#################################333333

v_allexpense = StringVar()

L = ttk.Label(T3,text = 'ยอดรวมทั้งหมด (บาท):',font=FONT1).place(x=50,y=50)
LR1 = ttk.Label(T3, textvariable=v_allexpense,font=FONT2)
LR1.place(x=200,y=45)

try:
	update_table()
	update_table2()
except:
	print('ERROR')

update_table()
GUI.mainloop()




