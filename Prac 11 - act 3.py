from tkinter import*

my_app = Tk(className= 'Simple Calculator')
L1 = Label(my_app, text= 'Geometry', font= ('Arial', 24))
L1.grid(row=0, column=0, columnspan=3, sticky= 'w')
L2 = Label(my_app, text= 'Calculate Square Area, A brick for example, Formula : Side x Side ')
L2.grid(row=1, column=0, columnspan=3, sticky= 'w')
L3 = Label(my_app, text= 'Side :')
L3.grid(row=3, column=0, columnspan=3, sticky= 'w')
E3 = Entry(my_app)
E3.grid(row=3, column=1, sticky='w')
L4 = Label(my_app, text='Area:')
L4.grid(row=4, column=1, sticky='w')
Area = StringVar()
L5 = Label(my_app, textvariable= Area)
L5.grid(row=4, column=2, sticky= 'w')

def calculate():
           Area.set(int(E3.get())**2)

B1= Button(my_app, text= 'calculate Area', command= calculate)
B1.grid(row=4, column=0, sticky= 'w')

my_app.mainloop()
