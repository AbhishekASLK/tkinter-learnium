from tkinter import *

class CardGenerator:
    def __init__(self):
        
        self.root = Tk()
        self.root.title('Card Generator')
        self.root.geometry('500x600')
        
        # ======================= Name =========================
        # Create a label for name
        self.name = Label(text='Full Name: ')
        self.name.pack()
        
        # Create Entry for name
        self.name_input = Entry(textvariable='Hi')
        self.name_input.pack()
        
        # ======================= Age =========================
        # Create a label for age
        self.age = Label(text='Age: ')
        self.age.pack()
        
        # Create Entry for age
        self.age_input = Entry()
        self.age_input.pack()
        
        # ======================= Email =========================
        # Create a label for Email
        self.email = Label(text='Email: ')
        self.email.pack()
        
        # Create Entry for email
        self.email_input = Entry()
        self.email_input.pack()
        
        # ======================= Checkbox =========================
        # Checkbutton
        self.checkbox = Checkbutton(text='Do you work?')
        self.checkbox.pack()        
        
        # ======================= Company =========================
        # Create a label for Company Name
        self.company = Label(text='Company Name: ')
        self.company.pack()
        
        # Create Entry for email
        self.company_input = Entry()
        self.company_input.pack()
        
        # ======================= Package =========================
        # Create a label for Package Name
        self.package = Label(text='Package: ')
        self.package.pack()
        
        # Create Entry for package
        self.package_input = Entry()
        self.package_input.pack()
        
        # ======================= Generate Button =========================
        # Create a label for Generate Button
        self.button = Button(text='Generate Card',bg='green',command=self.generateCard)
        self.button.pack(pady=20)  
        
    def generateCard(self):
        
        # Create Frame
        self.frame = Frame(self.root,height=200,width=70,bg='green')
        self.frame.pack(pady=5)
        
        # Display Name
        self.label = Label(self.frame,text='Full Name: '+self.name_input.get(),bg='green',justify='left')
        self.label.config(fg='white')
        self.label.pack(anchor='w')
        
        # Display Age
        self.label = Label(self.frame,text='Age: '+self.age_input.get(),bg='green',justify='left')
        self.label.config(fg='white')
        self.label.pack(anchor='w')
        
        # Display Email
        self.label = Label(self.frame,text='Email: '+self.email_input.get(),bg='green',justify='left')
        self.label.config(fg='white')
        self.label.pack(anchor='w')
        
        # Display Company
        self.label = Label(self.frame,text='Company: '+self.company_input.get(),bg='green',justify='left')
        self.label.config(fg='white')
        self.label.pack(anchor='w')
        
        # Display Package
        self.label = Label(self.frame,text='Package: '+self.package_input.get(),bg='green',justify='left')
        self.label.config(fg='white')
        self.label.pack(anchor='w')

    def run(self):
        self.root.mainloop()
    
if __name__ == '__main__':
    app = CardGenerator()
    app.run()




