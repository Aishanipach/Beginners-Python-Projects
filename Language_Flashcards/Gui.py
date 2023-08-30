import tkinter as tk
from PIL import ImageTk,Image


# Class for initial an image 
class Img(tk.Frame):
    #here i init the requared parameters for the Img class
    def __init__(self, parent, image_path):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        #image path the path where the image stored 
        self.image_path = image_path
        self.running = None

        #this is the function that i put bellow to render the ui element 
        self.initialize()
    def initialize(self):
        #open the image 
        self.image = Image.open(self.image_path)
        #than resize it to the requared size 
        self.resized_image = self.image.resize(size=(190,250))
        #than make the tkinter ui element that i will use for desplay the image 
        self.Tkimage = ImageTk.PhotoImage(self.resized_image)

# Class for a frame containing word and image
class Card_frame(tk.Frame):
    def __init__(self, parent):
        #the same logic when aver we want to creat a clas that inherit from tkinter class
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.running = None
        self.initialize()
    def initialize(self):
        # Create a frame that i will render in main app 
        self.frame = tk.Frame(self.parent,height=300,width=240,bg="#EAE5E5")
        # Initialize WoordImage to display an image e
        self.image = Img(self.frame,"imgs/apple.png")
        self.image_Label = tk.Label(master=self.frame,width=190,height=250,image=self.image.Tkimage)
        # Label to display the word "Appel" with specific styling
        self.woord = tk.Label(master=self.frame,text="Appel",bg="#F5F2F2",fg="#000000",
                font=("Arial", 12, "bold"),padx=10,pady=5)
        
        # Place the frame, and image & word label within the parent frame
        self.frame.place(relx=.5, rely=.4,anchor= tk.CENTER)
        self.image_Label.place(relx=.5,rely=.4,anchor=tk.CENTER)
        self.woord.place(relx=.5,rely=.9,anchor=tk.CENTER)

# Class for creating custom buttons       
class Button(tk.Button):
    def __init__(self, parent, background_coolor:str , foreground_coolor:str , active_coolor:str,btn_text:str
                 ,relX : float):
        tk.Button.__init__(self, parent)
        self.parent = parent
        self.background_coolor = background_coolor
        self.foreground_coolor= foreground_coolor
        self.active_coolor =active_coolor
        self.btn_text =btn_text
        self.relX = relX
        self.running = None
        self.initialize()
    def initialize(self):
        self.button = tk.Button(self.parent,height=2,width=10,bg=self.background_coolor,
                    fg=self.foreground_coolor,text=self.btn_text,activebackground=self.active_coolor)
        self.button.place(relx=self.relX,rely=.72,anchor=tk.NE)
class Main_app(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.running = None
        self.initialize()
    def initialize(self):
        self.card_frame = Card_frame(self)
        self.next_button = Button(self,"#0E9594","#ffffff","#127475","Next Woord",.87)
        self.previos_button = Button(self,"#344994","#ffffff","#2E4082","Previos Woord",.29)


if __name__ == "__main__":
    app = Main_app(None)
    app.title('my application')
    app.geometry("500x600")
    app.resizable(False, False)
    app.mainloop()