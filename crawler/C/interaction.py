import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("hello world")
root.geometry('1000x800')

Label(root, text='校训'.decode('gbk').encode('utf8'), font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text='厚德'.decode('gbk').encode('utf8'), font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='博学'.decode('gbk').encode('utf8'), font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='敬业'.decode('gbk').encode('utf8'), font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='乐群'.decode('gbk').encode('utf8'), font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

root.mainloop()