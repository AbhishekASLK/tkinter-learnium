from tkinter import *

# Create a window
root = Tk()

# Create label
myLabel1 = Label(root,text='Label 1')
myLabel2 = Label(root,text='Label 2')

# Put it on screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=10)

# program should run in loop
root.mainloop()