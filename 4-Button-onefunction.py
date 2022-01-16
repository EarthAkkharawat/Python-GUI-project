from tkinter import*
from tkinter import ttk

#GUI can change to any word such as root.
GUI = Tk() #This is the main window of program.
GUI.geometry('500x300') #Adjust the box size.
GUI.title('Example')

expenselist = {'fried_chicken':{'name':'ไก่ทอด','price':40}
               ,'coffee':{'name':'กาเเฟ','price':50},
               'Taxi':{'name':'เเท็กซี่','price':100}}


########### Function ############################################

def Expense(keyword):
    price = expenselist[keyword]['price']
    print('Expenditure: ' + expenselist[keyword]['name'])
    print('Cost: ' ,price)

########### ROW1 ##############################################

F1 = Frame(GUI)# F1 is a frame
#Frame is like a white-board 
F1.place(x= 20, y = 50)
# .place is for specify the position.

B1 = ttk.Button(F1, text = 'fried_chicken', command = lambda x= 'fried_chicken': Expense(x)) 
B1.grid(row = 0, column = 0, ipadx = 20, ipady = 10, padx = 5)

B2 = ttk.Button(F1, text = 'coffee', command = lambda x= 'coffee': Expense(x))
B2.grid(row = 0, column = 1, ipadx = 20, ipady = 10, padx = 5)

B3 = ttk.Button(F1, text = 'Taxi', command = lambda x= 'Taxi': Expense(x))#This button attach to F1.
B3.grid(row = 0, column = 2, ipadx = 20, ipady = 10, padx = 5)
# lambda is a special function, use for reduce many functions to one function..

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


