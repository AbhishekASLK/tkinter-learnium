from tkinter import *
from PIL import Image, ImageTk
import os

class ImageViewer:
    
    counter = 1
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Image Viewer')
        self.root.geometry('400x600')
        self.root.config(background='black')
        
        # Defines the Interface of Application
        self.GUI()
        
    def GUI(self):
        files = os.listdir('images')
        self.img_array = []
        for file in files:
            img = Image.open(os.path.join('images',file))
            resized_image = img.resize((200,300))
            self.img_array.append(ImageTk.PhotoImage(resized_image))
            
        self.img_label = Label(self.root,image=self.img_array[0])
        self.img_label.pack(pady=(15,20))

        next_btn = Button(self.root,text='Next',background='white',fg='black',width=25,height=2,command=self.next_img)
        next_btn.pack()
        
    def next_img(self):
        global counter
        self.img_label.config(image=self.img_array[self.counter%len(self.img_array)])
        self.counter = self.counter+1

    def run(self):
        self.root.mainloop()