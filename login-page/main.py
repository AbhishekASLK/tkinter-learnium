from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class LoginPage:
    def __init__(self):
        
        # Setting the screen
        self.root = Tk()
        self.root.title('Login Page')
        self.root.geometry('900x600')
        
        # Welcome Label
        self.welcome_label = Label(self.root, text="Welcome to Dev Community", font=("Helvetica", 20), fg='black')
        self.welcome_label.pack(pady=(30,5))
        
        # Add logo
        self.logo_img = Image.open('assets/logo.png')
        self.logo_img_resize = self.logo_img.resize((200,200))
        self.logo_img = ImageTk.PhotoImage(self.logo_img_resize)
        self.logo_label = Label(self.root,image=self.logo_img)
        self.logo_label.pack()
        
        # Email Label
        self.email_label = Label(self.root,text="Enter your email",font='40')
        self.email_label.pack()
        
        # Email Input
        self.email_input = Entry(self.root,width=30) 
        self.email_input.pack(ipady=5)
        
        # Password Label
        self.password_label = Label(self.root,text="Enter your password",font='40')
        self.password_label.pack()
        
        # Password Input
        self.password_input = Entry(self.root,width=30)
        self.password_input.pack(ipady=5)
        
        # Login Button
        self.login_button = Button(text='Login',command=self.authenticate)
        self.login_button.pack(pady=(10,10))
        
    def authenticate(self):
        email_input = self.email_input.get()
        password_input = self.password_input.get()
        if(email_input=='abhishekaslk@gmail.com' and password_input=='1234'):
            messagebox.showinfo('Successful','Successfully Logged in!')
        else:
            messagebox.showerror('Unsuccessful','Invalid email or password')
        
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = LoginPage()
    app.run()
