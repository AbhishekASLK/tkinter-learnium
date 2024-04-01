from tkinter import *

# create instance of Tk class
root = Tk()

# Set label to window
root.title('App')

# Set the geometry of screen
root.geometry('580x380')

# Adding text label to screen
label = Label(text='Demo App',font='24')

# Pack to the screen (pack: geometry manager)
label.pack()

root.mainloop()