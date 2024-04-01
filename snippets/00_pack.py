from tkinter import *

# Create a window
root = Tk()

# To Show anything on screen, there is 2 step process in tkinter
# 1. Define the things
# 2. Put it to the screen

# Create label
myLabel = Label(root,text='Hello World!')

# Put it on screen
myLabel.pack()

# program should run in loop
root.mainloop()