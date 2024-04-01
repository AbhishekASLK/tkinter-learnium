# ================= padx and ipadx ===================

import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title('Frame')
root.geometry('400x600')

# Top Frame
top_frame = ttk.Frame()

# Widgets
label1 = ttk.Label(top_frame,text='Label 1',background='red')
label2 = ttk.Label(top_frame,text='Label 2',background='blue')
label1.pack()
label2.pack()

# Even thought label1 and label2 are packed but will not visible until we pack the frame to the root
top_frame.pack()

label3 = ttk.Label(text='Label 3',background='green')
label3 = ttk.Label(text='Label 3',background='orange')
button = ttk.Button(text='Button1')
button = ttk.Button(text='Button2')

# layout


root.mainloop()