from tkinter import *
import random
import time

mainWin = Tk()
mainWin.geometry('800x500+100+100')
mainWin.title('Bill Generation System')

Tops = Frame(mainWin,width=1200,height=50,bg='green',relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(mainWin, width=800, height=700,bg='blue',relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(mainWin, width=300, height=700,bg='red',relief=SUNKEN)
f1.pack(side=RIGHT)

localTime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial',30,'bold'), text='Billing System', fg='Steel Blue', bd=10, anchor ='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'), text=localTime, fg='Steel Blue', bd=10, anchor ='w')
lblInfo.grid(row=1,column=0)

mainWin.mainloop()