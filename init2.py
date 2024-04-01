from tkinter import *

root = Tk() 							# Create the root (base) window 
root.geometry('300x300')
root.config(background='red')

w = Label(root, text="Hello, world!") 	# Create a label with words

w.pack() 								# Put the label into the window

root.mainloop()