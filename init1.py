from tkinter import *

class HelloWorld:
    def __init__(self):
        
        # Create Tk class object
        self.root = Tk()
        
        # Set the window title
        self.root.title('Hello World App')
        
        # Set the geometry of opening screen
        self.root.geometry('500x500')
        
        # Set the text label
        self.message_label = Label(self.root,text='',fg='black')
        self.message_label.pack(pady=(10,5))
        self.message_label.config(font=('verdana',20))
        
        # Button
        self.button = Button(self.root,text='Click me',command=self.message)
        self.button.pack(pady=(5,20))
        
    def message(self):
        self.message_label.config(text='Hello Duniya')
    
    def run(self):
        self.root.mainloop()
        
if __name__ == '__main__':
    root = HelloWorld()
    root.run()
        