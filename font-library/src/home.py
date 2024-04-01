from PIL import Image,ImageTk
import tkinter as tk
import os
from tkinter import ttk, messagebox

class LibraryApp:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.title('Tkinter Library')
        
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg='#192f44')
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create the main background frame
        self.background_frame = tk.Frame(self.root,bg='#0A2472',width=self.screen_width,height=self.screen_height)
        self.background_frame.pack()
        
        # Create left frame
        self.left_frame = tk.Frame(self.background_frame,bg='#00072D',width=self.screen_width//6,height=self.screen_height)
        self.left_frame.pack(side=tk.LEFT)
        
        # Set up button styling
        style = ttk.Style()
        style.configure("Rounded.TButton",borderwidth=0,relief='flat',background='#BCD2E8',padding=10,font=('Poppins',12))
        style.map("Rounded.TButton",foreground=[('pressed','black'),('active','white')])
        
        self.button_label = ttk.Button(self.left_frame,text='Font Library',style="Rounded.TButton",command=self.show_font_tab)
        self.button_label.pack()
        self.button_label.place(x=60,y=350,anchor='nw')
        
        # Load and display an image
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory,"../assets/logo.jpg")
        img = ImageTk.PhotoImage(Image.open(img_path).resize((200,100)))
        self.label = tk.Label(self.left_frame,image=img,background='#00072D')
        self.label.image = img
        self.label.pack()
        self.label.place(x=40,y=20,anchor='nw')
        
        # Set up the right frame for dynamic content
        rgba_color = (222,55,48,255)
        tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])
        self.right_frame = tk.Frame(self.background_frame,bg='#BCD2E8',width=(self.screen_width-self.screen_width//6),height=self.screen_height)
        self.right_frame.pack(side=tk.RIGHT)
        
        # Set up a label with welcome text
        
        self.original_label_text = "Welcome to Core2Web"
        self.right_label = tk.Label(self.right_frame,text=self.original_label_text,background='#BCD2E8',font=('Poppins',50,'bold'),fg=tk_color)
        self.right_label.pack()
        self.right_label.place(x=300,y=300,anchor='nw')
        
        # Create a 'Back Button'
        self.back_button = ttk.Button(self.left_frame,text='Back',style="Rounded.TButton",command=self.reset_ui)
        self.back_button.pack()
        self.back_button.place(x=60,y=400,anchor='nw')
        
        # Track whether Font Library is open
        self.font_library_opened = False
        
        self.additional_widgets = []
        
    def show_font_tab(self):
        if self.font_library_opened:
            messagebox.showinfo("Already Opened",'Font Library is already opened')
        else:
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []
            
            # Set up font Library tab
            rgba_color = (222,55,48,255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])
            
            # Create and pack widgets
            self.heading_label = tk.Label(self.right_frame,text='Font Library',background='#BCD2E8',font=('Poppins',20,'bold'),fg=tk_color)
            self.heading_label.pack()
            self.heading_label.place(x=60*2,y=150,anchor='nw')
            
            self.input_label = ttk.Entry(self.right_frame,width=60,font=("Poppins",12))
            self.input_label.insert(0,"Enter your text here..")
            self.input_label.pack()
            self.input_label.place(x=60*2,y=200,anchor='nw')
            
            self.right_label.config(text='')
            self.font_library_opened = True
            
            # Create buttons for different fonts
            self.button_label1 = ttk.Button(self.right_frame,text='Poppins',style='Rounded.TButton',command=self.poppinClicked)
            self.button_label1.pack()
            self.button_label1.place(x=60*2,y=350,anchor='nw')
            
            self.button_label2 = ttk.Button(self.right_frame,text='Modern',style='Rounded.TButton',command=self.modernClicked)
            self.button_label2.pack()
            self.button_label2.place(x=60*5,y=350,anchor='nw')
            
            self.button_label3 = ttk.Button(self.right_frame,text='Courier',style='Rounded.TButton',command=self.courierClicked)
            self.button_label3.pack()
            self.button_label3.place(x=60*8,y=350,anchor='nw')
            
            self.button_label4 = ttk.Button(self.right_frame,text='Sans Serif',style='Rounded.TButton',command=self.sanserifClicked)
            self.button_label4.pack()
            self.button_label4.place(x=60*11,y=350,anchor='nw')
            
            self.button_label5 = ttk.Button(self.right_frame,text='Calibri',style='Rounded.TButton',command=self.calibriClicked)
            self.button_label5.pack()
            self.button_label5.place(x=60*14,y=350,anchor='nw')
            
            self.show_label = tk.Label(self.right_frame,text='',background='#BCD2E9',font=('Poppins',50,'bold'),fg=tk_color)
            self.show_label.pack()
            self.show_label.place(x=60*2,y=500,anchor='nw')
            
    def poppinClicked(self):
        self.show_label.config(text=self.input_label.get(),font=('Poppins',30,'bold'))
        
    def modernClicked(self):
        self.show_label.config(text=self.input_label.get(),font=('Modern',30,'bold'))
        
    def courierClicked(self):
        self.show_label.config(text=self.input_label.get(),font=('Courier',30,'bold'))

    def sanserifClicked(self):
        self.show_label.config(text=self.input_label.get(),font=('MS Sans Serif',30,'bold'))

    def calibriClicked(self):
        self.show_label.config(text=self.input_label.get(),font=('Calibri',30,'bold'))
        
    def reset_ui(self):
        self.font_library_opened = False
        
        for widget in self.additional_widgets:
            widget.destroy()
            
        self.additional_widgets = []
        self.heading_label.destroy()
        self.input_label.destroy()
        self.button_label1.destroy()
        self.button_label2.destroy()
        self.button_label3.destroy()
        self.button_label4.destroy()
        self.button_label5.destroy()
        self.show_label.destroy()
        
        self.right_label.config(text=self.original_label_text)
    
    def run(self):
        self.root.mainloop()
        
        