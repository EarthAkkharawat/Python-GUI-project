from tkinter import*
from tkinter import ttk
from tkinter import messagebox

GUI = Tk() #This is the main window of program.
GUI.title('Example')

w = 500
h = 300

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws, hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #Adjust the box size.
#GUI.state('zoomed')
####################### RADIO BUTTON ########################################################################
#radiobox/button = button to check/choose.

F1 = Frame(GUI)
F1.pack(pady = 10)

v_radio = StringVar() #เก็บค่าจากการเลือก
RB1 = ttk.Radiobutton(F1, text = 'Pop up', variable = v_radio, value = 'popup')
RB2 = ttk.Radiobutton(F1, text = 'print', variable = v_radio, value = 'print')
RB1.pack()
RB2.pack()
RB1.invoke() #make RB1 = default

def Run():
	v = v_radio.get() #ดึงค่าจากตัวเเปรที่เก็บค่าของ radio
	print(v) 

	if v == 'popup':
		messagebox.showinfo('Popup', 'You are choosing popup') #show informing message
	else:
		print('You are not choosing popup, you chose print') 




B1 = ttk.Button(GUI, text = 'Run', command = Run)
B1.pack()

################## CHECK BUTTON ###################################################3
F2 = Frame(GUI)
F2.pack()


c1 = StringVar()
c1.set("Not rice") #set default value
c2 = StringVar()
c2.set('Not fish')
c3 = StringVar()
c3.set('Not water')

C1 = ttk.Checkbutton(F2, text = 'Rice',onvalue = 'Rice', offvalue = 'Not Rice', variable = c1)
C1.grid(row = 0, column = 1)
C1.invoke()

C2 = ttk.Checkbutton(F2, text = 'Fish', onvalue = 'Fish',offvalue = 'Not Fish', variable = c2)
C2.grid(row = 0, column = 2)

C3 = ttk.Checkbutton(F2, text = 'Water', onvalue = 'Water',offvalue = 'Not Water', variable = c3)
C3.grid(row = 0, column = 3)



def SelectFood():
	print(c1.get())
	print(c2.get())
	print(c3.get())
	print('-------')

B2 = ttk.Button(GUI,text='Select Food',command=SelectFood)
B2.pack()


#################### COMBO BOX #################################################
cblist = ['Credit', 'Cash', 'Banking']


CB1 = ttk.Combobox(GUI,values=cblist)
CB1.set('Cash')
CB1.place(x = 20, y = 200)

def Dropdown():
	print(CB1.get())

B3 = ttk.Button(GUI,text='Dropdown',command=Dropdown)
B3.place(x=200, y=200)






GUI.mainloop()#This input makes the program run all the time.
