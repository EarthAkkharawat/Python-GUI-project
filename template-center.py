from tkinter import*
from tkinter import ttk

GUI = Tk() #This is the main window of program.
GUI.title('Example')

w = 500
h = 300

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws, hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


GUI.geometry(f'{w} x {h} + {x: .0f} + {y:.0f}') #Adjust the box size.



GUI.mainloop()#This input makes the program run all the time.
