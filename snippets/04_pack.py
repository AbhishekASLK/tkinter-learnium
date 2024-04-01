# ================= expand and fill ===================

import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.title('Pack')
root.geometry('400x600')

# Widgets
label1 = ttk.Label(text='Label 1',background='red')
label2 = ttk.Label(text='Label 2',background='blue')
label3 = ttk.Label(text='Label 3',background='green')
button = ttk.Button(text='Button')

# layout
label1.pack(side='top',fill='x')
label2.pack(side='top',expand=True)
label3.pack(side='top',fill='both')
button.pack(side='top',fill='y')

root.mainloop()