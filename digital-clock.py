'''
Simple Digital clock GUI
Dev : AbdElrahman Youssef
Phone : 01141870926
Location : Egypt

'''
import time 
from time import strftime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
#-------------------------------------####  main Settings ######-----------------------------------
app1 = tk.Tk()
app1.config(bg='black')
app1.title('Simple Clock')
app1.resizable(False,False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~  Clock ~~~~~~~~~~ 12:25:31 PM ~~~~~~~~~~~~
def clock():
	x = strftime('%H:%M:%S %p')
	lbl.config(text=x)
	lbl.after(1000,clock)
lbl = tk.Button(app1,bg='black',fg='cyan',font=('tajawal',20,'bold'),command=countdown)
lbl.pack()


##################################
# call clock function

clock()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


app1.mainloop()

