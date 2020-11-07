from tkinter import *

root = Tk() #Makes the window
root.wm_title("Window Title") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF")


def redCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
    colorLog.insert(0.0, "Red\n")

def yelCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='yellow')
    colorLog.insert(0.0, "Yellow\n")

def grnCircle():
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='green')
    colorLog.insert(0.0, "Green\n")


#Left Frame and its contents
leftFrame = Frame(root, width=200, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

Label(leftFrame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)

Instruct = Label(leftFrame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
Instruct.grid(row=1, column=0, padx=10, pady=2)

try:
    imageEx = PhotoImage(file = 'image.gif')
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
except:
    print("Image not found")

#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=0, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200)
btnFrame.grid(row=1, column=0, padx=10, pady=2)

colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0)
colorLog.grid(row=2, column=0, padx=10, pady=2)

redBtn = Button(btnFrame, text="Red", command=redCircle)
redBtn.grid(row=0, column=0, padx=10, pady=2)

yellowBtn = Button(btnFrame, text="Yellow", command=yelCircle)
yellowBtn.grid(row=0, column=1, padx=10, pady=2)

greenBtn = Button(btnFrame, text="Green", command=grnCircle)
greenBtn.grid(row=0, column=2, padx=10, pady=2)


root.mainloop()