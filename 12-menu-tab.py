from tkinter import*
from tkinter import ttk

GUI = Tk() #This is the main window of program.
GUI.title('Example')
GUI.iconbitmap('wallet.ico')

w = 500
h = 300

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws, hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #Adjust the box size.


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






GUI.mainloop()




