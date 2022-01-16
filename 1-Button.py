from tkinter import*
from tkinter import ttk

#GUI can change to any words such as root.
GUI = Tk() #This is the main window of program.
GUI.geometry('500x300') #Adjust the box size.
GUI.title('Example')

B1 = Button(GUI, text = 'Hello')
B1.pack(pady = 10)#pady is to add 10 pixels space vertically between B1 and B2.



F1 = Frame(GUI)# F1 is a frame
#Frame is like a white-board 
F1.place(x= 20, y = 20)
#if not add frame, the code will be error.

B2 = ttk.Button(F1, text = 'HI, there')#GUI is a frame that is attached by 'Hi, there'
B2.pack(ipadx = 20, ipady = 10)#Adjusting size of the text box.

B3 = ttk.Button(F1, text = 'Save')#this button attach F1.
B3.pack(ipadx = 20, ipady = 10)





GUI.mainloop()#This input makes the program run all the time.
