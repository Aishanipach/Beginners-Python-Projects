import asyncio
import tkinter as tk
from PIL import ImageTk,Image
import json

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
        self.img_path =""
        self.woord =""
        self.data_index = 0
        self.running = None
        self.data = None
        self.initialize()
    def initialize(self):
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.initialize_data())

        self.img_path = self.data[self.data_index]["img_path"]
        self.woord = self.data[self.data_index]["woord"]

        # Create a frame that i will render in main app 
        self.frame = tk.Frame(self.parent,height=300,width=240,bg="#EAE5E5")
        # Initialize WoordImage to display an image e
        self.image = Img(self.frame,self.img_path)
        self.image_Label = tk.Label(master=self.frame,width=190,height=250,image=self.image.Tkimage)
        # Label to display the word "Appel" with specific styling
        self.woord_label = tk.Label(master=self.frame,text=self.woord,bg="#F5F2F2",fg="#000000",
                font=("Arial", 12, "bold"),padx=10,pady=5)
        
        # Place the frame, and image & word label within the parent frame
        self.frame.place(relx=.5, rely=.4,anchor= tk.CENTER)
        self.image_Label.place(relx=.5,rely=.4,anchor=tk.CENTER)
        self.woord_label.place(relx=.5,rely=.9,anchor=tk.CENTER)
    async def load_data(self):
        with open("eng.json","r") as json_file:
            data = json.load(json_file)
        return data
    async def initialize_data(self):
        self.data = await self.load_data()
    def update(self):
        self.img_path = self.data[self.data_index]["img_path"]
        self.woord = self.data[self.data_index]["woord"]
        # Initialize WoordImage to display an image e
        self.image = Img(self.frame,self.img_path)
        self.image_Label.config(image=self.image.Tkimage)
        self.woord_label.config(text=self.woord)
    def next(self):
        if(self.data_index < len(self.data)-1):
            self.data_index = self.data_index + 1
            self.update()
    def previous(self):
        if(self.data_index > 0):
            self.data_index = self.data_index - 1
            self.update()
# Class for creating custom buttons       
class Button(tk.Button):
    def __init__(self, parent, background_coolor:str , foreground_coolor:str , active_coolor:str,btn_text:str
                 ,relX : float , command=None):
        tk.Button.__init__(self, parent)
        self.parent = parent
        self.background_coolor = background_coolor
        self.foreground_coolor= foreground_coolor
        self.active_coolor =active_coolor
        self.btn_text =btn_text
        self.relX = relX
        self.command =command
        self.running = None
        self.initialize()
    def initialize(self):
        self.button = tk.Button(self.parent,height=2,width=11,bg=self.background_coolor,
                    fg=self.foreground_coolor,text=self.btn_text,
                    activebackground=self.active_coolor, command=self.command)
        
        self.button.place(relx=self.relX,rely=.72,anchor=tk.NE )
class Main_app(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.running = None
        self.initialize()
    def initialize(self):
        self.card_frame = Card_frame(self)
        self.next_button = Button(self,"#0E9594","#ffffff","#127475",
                                  "Next Woord",.87,command=self.card_frame.next)
        self.previos_button = Button(self,"#344994","#ffffff","#2E4082",
                                     "Previos Woord",.29,command=self.card_frame.previous)


