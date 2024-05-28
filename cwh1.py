from tkinter import *

a= Tk()

#gui logic
#in min geometry module (width,height) is written
a.geometry("444x234")
pic=PhotoImage(file="pics_for_app\dock")
ab=Label(image=pic)
ab.pack()
a.minsize(200,100)
a.maxsize(1200,988)
b=Label(text="This is my first gui application of python")
b.pack()
a.mainloop()

