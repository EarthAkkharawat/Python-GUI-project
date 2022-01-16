from tkinter import*
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x500')
G = Canvas(GUI,width=400,height=300)
G.place(x=0,y=0)


def UpdateGraph(expense=100,income=200):
	
	if income >= expense:
		ep = int((expense / income) * 300)
		ic = 298
	else:
		ic = int((income/expense) * 300)
		ep = 298
	



	start_y = 300
	total = 300



	print('income', ic)
	print('Expense', ep)
	hb1 = ep
	hb2 = ic
	hb3 = hb2 - hb1

	G.delete(ALL)

	b1 = G.create_rectangle(50,total - hb1,100,start_y,fill='orange')
	b2 = G.create_rectangle(150,total - hb2,200,start_y,fill='green')
	b3 = G.create_rectangle(250,total - hb3,300,start_y,fill='blue')


	L = ttk.Label(GUI,text='Expense').place(x=100,y=370)
	L = ttk.Label(GUI,text='Income').place(x=200,y=370)
	L = ttk.Label(GUI,text='Remaining').place(x=300,y=370)











UpdateGraph(1000,5000)



GUI.mainloop()