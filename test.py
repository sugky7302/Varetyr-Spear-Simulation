from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

def getInt (v) :
    s = v.get()
    return str(2.5 * int(s))

def cal ():
    label.config(text = getInt(value))

def NewEntry (labelText, column, row):
    newObject = {}
    newObject['label'] = ttk.Label(window, text = labelText)
    newObject['label'].grid(column = column, row = row)
    newObject['value'] = StringVar()
    newObject['entry'] = ttk.Entry(window, width = 4, textvariable = newObject['value'])
    newObject['entry'].grid(column = column + 1, row = row)
    return newObject

# 創建主視窗
window = Tk()
value = StringVar()
entry = ttk.Entry(window, width = 4, textvariable = value)
entry.grid(column = 0, row = 0)
button = ttk.Button(window, text = "test", command = cal)
button.grid(column = 1, row = 0)
label = ttk.Label(window)
label.grid(column = 0, row = 1)
abc = NewEntry("123", 0, 2)
window.mainloop()