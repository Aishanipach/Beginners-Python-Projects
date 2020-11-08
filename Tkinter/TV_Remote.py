#A TV Remaote GUI ( turns TV on/off, sets Volume and change channels)
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
            
            circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
            colorLog.insert(0.0, "TV is Turned ON\n")  
        else:
            self.on=False
            circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='grey')
            colorLog.insert(0.0, "TV is Turned OFF\n")    


    
    
    def setChannel(self,c=-1):
        if(self.channel<10 and self.on==True):
            self.channel=c
            btnLog.insert(0.0, "Current Channel:{} \n" .format(self.channel))
        elif(self.on==False):
            colorLog.insert(0.0, "Turn on the TV \n")
        else:
            colorLog.insert(0.0, "Wrong Input \n")
            
    def getVolume(self):
        return(self.vol)

    def setVolume(self,volume):
        if(self.on==True):
            rectangleCanvas.create_rectangle(20, 20,300,80, width=0, fill='white')
            self.vol=volume
            l=(30*volume)
            print(l)
            rectangleCanvas.create_rectangle(20, 20,l, l, width=0, fill='red') 
            btnLog.insert(0.0, "volume set to {}\n".format(self.vol))
        else:
            btnLog.insert(0.0, "Turn on the TV \n")
    
    def channelUp(self):
        if(self.channel<10 and self.on==True):
            self.channel+=1
            colorLog.insert(0.0, "Current Channel:{} \n" .format(self.channel))
        elif(self.on==False):
            colorLog.insert(0.0, "Turn on the TV \n")
        else:
            colorLog.insert(0.0, "No further channels available \n")    

    def channelDOWN(self):
        if(self.channel>0 and self.on==True):
            self.channel-=1
            colorLog.insert(0.0, "Current Channel:{} \n" .format(self.channel))
        elif(self.on==False):
            colorLog.insert(0.0, "Turn on the TV \n")
        else:
            colorLog.insert(0.0, "No negative Channels \n")    

    
    def VolumeUp(self):
        if(self.vol<5 and self.on==True):
            self.vol+=1
            colorLog.insert(0.0, "Current Volume:{} \n" .format(self.vol))
        elif(self.on==False):
            colorLog.insert(0.0, "Turn on the TV \n")
        else:
            colorLog.insert(0.0, "Max Volume \n") 

    def VolumeDown(self):
        if(self.vol>0 and self.on==True):
            self.vol-=1
            colorLog.insert(0.0, "Current Volume:{} \n" .format(self.vol))
        elif(self.on==False):
            colorLog.insert(0.0, "Turn on the TV \n")
        else:
            colorLog.insert(0.0, "MUTE \n") 





        

t1= TV()

root = Tk()
w = Label(root, text=" TV Remote!")
k = Button(root,activebackground="black", text= "Hi")

#Turn ON & Turn OFF, Volume, Channel UP &DOWN
rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=0, column=0, padx=10, pady=2)
        
btnFrame = Frame(rightFrame, width=200, height = 400)
btnFrame.grid(row=1, column=0, padx=10, pady=2)
colorLog = Text(rightFrame, width = 30, height = 20, takefocus=0)
colorLog.grid(row=2, column=0, padx=10, pady=2)


if(t1.on==False):
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='grey')
    colorLog.grid(row=2, column=0, padx=10, pady=2)
    

redBtn = Button(btnFrame, text="Turn On", command=t1.turnON)
redBtn.grid(row=0, column=0, padx=10, pady=2)


yellowBtn = Button(btnFrame, text="Channel UP", command=t1.channelUp)
yellowBtn.grid(row=1, column=1, padx=10, pady=2)

greenBtn = Button(btnFrame, text="Channel DOWN", command=t1.channelDOWN)
greenBtn.grid(row=1, column=2, padx=10, pady=2)

purpleBtn = Button(btnFrame, text="Volume UP", command=t1.VolumeUp)
purpleBtn.grid(row=2, column=1, padx=10, pady=2)

purpleBtn = Button(btnFrame, text="Volume DOWN", command=t1.VolumeDown)
purpleBtn.grid(row=2, column=2, padx=10, pady=2)

#Left frame
leftFrame = Frame(root, width=400, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)
btnLog = Text(leftFrame, width =20, height = 20, takefocus=0)
btnLog.grid(row=1, column=0, padx=10, pady=2)
btnFrame = Frame(leftFrame, width=200, height = 100)
btnFrame.grid(row=2, column=0, padx=10, pady=2)
rectangleCanvas = Canvas(leftFrame, width=150, height=30, bg='white')
rectangleCanvas.grid(row=3, column=0, padx=10, pady=2)
#Channel Number 
one = Button(btnFrame, text="1", command=lambda:t1.setChannel(1))
one.grid(row=0, column=0, padx=10, pady=2)

two = Button(btnFrame, text="2", command=lambda:t1.setChannel(2))
two.grid(row=0, column=1, padx=10, pady=2)

three = Button(btnFrame, text="3", command=lambda:t1.setChannel(3))
three.grid(row=0, column=2, padx=10, pady=2)

four = Button(btnFrame, text="4", command=lambda:t1.setChannel(4))
four.grid(row=1, column=0, padx=10, pady=2)

five = Button(btnFrame, text="5", command=lambda:t1.setChannel(5))
five.grid(row=1, column=1, padx=10, pady=2)

six = Button(btnFrame, text="6", command=lambda:t1.setChannel(6))
six.grid(row=1, column=2, padx=10, pady=2)

seven = Button(btnFrame, text="7", command=lambda:t1.setChannel(7))
seven.grid(row=2, column=0, padx=10, pady=2)

eight = Button(btnFrame, text="8", command=lambda:t1.setChannel(8))
eight.grid(row=2, column=1, padx=10, pady=2)

nine = Button(btnFrame, text="9", command=lambda:t1.setChannel(9))
nine.grid(row=2, column=2, padx=10, pady=2)
#Set Volume
vone = Button(btnFrame, text="Vol1", command=lambda:t1.setVolume(1))
vone.grid(row=4, column=0, padx=10, pady=2)

vtwo = Button(btnFrame, text="Vol2", command=lambda:t1.setVolume(2))
vtwo.grid(row=4, column=1, padx=10, pady=2)

vthree = Button(btnFrame, text="Vol3", command=lambda:t1.setVolume(3))
vthree.grid(row=4, column=2, padx=10, pady=2)

vfour = Button(btnFrame, text="Vol4", command=lambda:t1.setVolume(4))
vfour.grid(row=4, column=3, padx=10, pady=2)

vfive = Button(btnFrame, text="Vol5", command=lambda:t1.setVolume(5))
vfive.grid(row=4, column=4, padx=10, pady=2)


root.mainloop()
w.pack()
k.pack()


