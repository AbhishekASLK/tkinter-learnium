from tkinter import *
import requests
from urllib.request import urlopen
import io
from PIL import Image,ImageTk
import webbrowser

class NewsApp:
    
    def __init__(self):
        
        # Fetch the data using the requests module in json format
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=92b0d30aa4c941d18bec50e86abdd320').json()
        
        # Initial UI
        self.initialUI()
        
        # Load the 1st NEWS Item
        self.newsItem(0)
        
        # Stay running the instance of the program
        self.run()
        
    def initialUI(self):
        self.root = Tk()
        self.root.title('inshorts App')
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.config(background='white')
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
    def newsItem(self,index):


        # clear screen for next news, old should be vanished
        self.clear()
        
        # ==================== Image of News Item ========================
        
        # If there is an issue with fetching the image then local image will be load
        # so that's why it should be in try block
        try:
            # Get the URL of Image
            self.image_url = self.data['articles'][index]['urlToImage']
            
            # Open the URL of Image
            self.response = urlopen(self.image_url)
            
            # Read the URL of Image and we wil get the raw binary format data
            self.raw_image_data = self.response.read()
            
            # Convert data data into image format and opened it
            self.image = Image.open(io.BytesIO(self.raw_image_data)).resize((350,250))
            
            # Make it an normal image
            self.image = ImageTk.PhotoImage(self.image)
            
            # Created the label for image to display on screen
            self.image_label = Label(image=self.image)
            
            # Pack it to the screen using pack() geometry manager
            self.image_label.pack()
            
        except:
            self.response = urlopen('https://www.ncenet.com/wp-content/uploads/2020/04/No-image-found.jpg')
            self.image = self.response.read()
            self.image = Image.open(io.BytesIO(self.image))
            self.image_label = Label(image=self.image)
            self.image_label.pack()
         
        # ==================== Heading of News Item ========================   
        
        # Getting the heading of the news item
        self.heading = self.data['articles'][index]['title']
        
        # Creating the label for that news heading
        self.heading_label = Label(text=self.heading,font=('Verdana',14,'bold'),wraplength=330,background='white',justify=LEFT)
        
        # Packing it into the screen
        self.heading_label.pack(pady=30)
        
        # ==================== Description of News Item ========================
        
        # Getting the description of an news item
        self.description = self.data['articles'][index]['description']
        
        # Creating the label for the description 
        self.description_label = Label(text=self.description,wraplength=330,font=('Verdana',11),background='white',justify=LEFT)
        
        # Packing it into the screen
        self.description_label.pack()
        
        
        # ==================== Navigation Buttons for Items ========================
        
        # Prev Button
        if index !=0:
            self.prev_btn = Button(text='Prev',font=('Verdana',9,'bold'))
            self.prev_btn.pack(side=LEFT,expand=True)
        
        # Read Button
        self.read_btn = Button(text='Read',font=('Verdana',9,'bold'),command=lambda:self.read_more(self.data['articles'][index]['url']))
        self.read_btn.pack(side=LEFT,expand=True)
        
        # Next Button
        if len(self.data['articles']) != index+1:
            self.next_btn = Button(text='Next',font=('Verdana',9,'bold'),command=lambda:self.newsItem(index+1))
            self.next_btn.pack(side=LEFT,expand=True)
        
    def read_more(self,url):
        webbrowser.open(url)
            
    def run(self):
        self.root.mainloop()
        
