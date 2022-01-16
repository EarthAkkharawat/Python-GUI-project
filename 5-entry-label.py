from tkinter import*
from tkinter import ttk

GUI = Tk() #This is the main window of program.
GUI.geometry('500x300') #Adjust the box size.
GUI.title('Example')

FONT1 = ('Angsana New', 15)
FONT2 = ('Angsana New', 20, 'bold')

# v_expense use for store value that typed by user.
v_expense = StringVar()

# E1 is a box to fill text.
L = ttk.Label(GUI, text = 'Please fill your expense').pack() #topic above E1
E1 = ttk.Entry(GUI, textvariable=v_expense, font = FONT1, width = 30)
E1.pack(pady = 10)

# v_price use for store value that typed by user.
v_price = StringVar()

# E2 is a box to fill text.
L = ttk.Label(GUI, text = 'Expense (baht)').pack() #topic above E2
E2 = ttk.Entry(GUI, textvariable=v_price, font = FONT1, width = 30)
E2.pack(pady = 10)

# SaveExpense is function when button is clicked, this function will work.
def SaveExpense(event = None):
    exp = v_expense.get()
    pc = float(v_price.get()) #transforming striing to float
    print('list: ', exp) # v_expense.get() is to pull the value to use 
    #v_result.set('You are saving list: ' + exp + ' price: '+ v_price.get() + ' baht') should not use this method
    v_result.set(f'Saving your lists : {exp} price : {pc:,.2f} baht') #should use this format method.

    #reset variables
    v_expense.set('')
    v_price.set('')
    #make cursor automatically moves to E1 box.
    E1.focus()

    
E2.bind('<Return>',SaveExpense) #if using "bind", it have to input "event = none" in function

# B1 is a save button.
B1 = ttk.Button(GUI, text = 'Save', command = SaveExpense)
B1.pack()

#######LABEL############
v_result = StringVar()
R1 = ttk.Label(GUI, textvariable = v_result, font = FONT2, foreground = 'green')
R1.pack(pady = 20)

GUI.mainloop()#This input makes the program run all the time.
