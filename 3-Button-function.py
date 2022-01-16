from tkinter import*
from tkinter import ttk

#GUI can change to any word such as root.
GUI = Tk() #This is the main window of program.
GUI.geometry('500x300') #Adjust the box size.
GUI.title('Example')
###########Function############################################

def Expensefried_chicken():  #Expense is function's name.
    print('You have the cost: fried_chicken 40 baht')

def Expensecoffee():  
    print('You have the cost: coffee 50 baht')

def ExpenseTaxi():
    print('You have the cost: Taxi 100 baht')

########### ROW1 ##############################################

F1 = Frame(GUI)# F1 is a frame
#Frame is like a white-board 
F1.place(x= 20, y = 50)
# .place is for specify the position.

B1 = ttk.Button(F1, text = 'fried_chicken', command = Expensefried_chicken)
B1.grid(row = 0, column = 0, ipadx = 20, ipady = 10, padx = 5)

B2 = ttk.Button(F1, text = 'coffee', command = Expensecoffee)
B2.grid(row = 0, column = 1, ipadx = 20, ipady = 10, padx = 5)

B3 = ttk.Button(F1, text = 'Taxi', command = ExpenseTaxi)#This button attach to F1.
B3.grid(row = 0, column = 2, ipadx = 20, ipady = 10, padx = 5)


########### ROW2 ##############################################

F2 = Frame(GUI)# F1 is a frame
#Frame is like a white-board 
F2.place(x= 20, y = 100)
# .place is for specify the position.

B1 = ttk.Button(F2, text = 'Soft drink')
B1.grid(row = 0, column = 0, ipadx = 21, ipady = 10, padx = 5)

B2 = ttk.Button(F2, text = 'Vegetables')
B2.grid(row = 0, column = 1, ipadx = 21, ipady = 10, padx = 5)

B3 = ttk.Button(F2, text = 'Bread')#This button attach to F1.
B3.grid(row = 0, column = 2, ipadx = 21, ipady = 10, padx = 5)


GUI.mainloop()#This input makes the program run all the time.


