from tkinter import *
import tkinter.messagebox
class TV:
    def __init__(self):
        self.channel=1
        self.vol=1
        self.on=False

    def turnON(self):
        if(self.on==False):
            self.on=True
            print("Hello, Tv is ON")
        else:
            print('It\'s already on')
    
    def turnOFF(self):
        if(self.on==True):
            self.on=False
            print("Bye!, TV is OFF")
        else:
            print("It's already OFF")

    def getChannel(self):
        return(self.channel)
    
    def setChannel(self,ch):
        self.channel=ch
        
    def getVolume(self):
        return(self.vol)

    def setVolume(self,volume):
        self.vol=volume
    
    def channelUp(self):
        self.channel+=1

    def channelDOWN(self):
        self.channel-=1
    
    def VolumeUp(self):
        self.vol+=1

    def VolumeDown(self):
        self.vol-=1

    def tvr(self):
        root = Tk()
        w = Label(root, text=" TV Remote!")
        k = Button(root,activebackground="black", text= "Hi")
        tkinter.messagebox.showinfo( "Hello Python", "Hello World")
        w.pack()
        k.pack()
        
        root.mainloop()
        w = Button(root,activebackground="black", text= "Hi")


t1= TV()

