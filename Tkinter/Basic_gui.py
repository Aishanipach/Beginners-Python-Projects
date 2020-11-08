#This is a reference code I used which covers most of the topics for basic GUI


from tkinter import *

root = Tk() #Makes the window
root.wm_title("Window Title") #Makes the title that will appear in the top left
root.config(bg = "#828481")

#It displays color button, which once clicked show mentioned color on the screen 
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
leftFrame = Frame(root, width=200, height = 600, bg="#C8F9C4", highlightthickness=2, highlightbackground="#111")
leftFrame.grid(row=0, column=0, padx=10, pady=2, sticky=N+S)

Inst = Label(leftFrame, text="Instructions:", anchor=W, bg="#C8F9C4")
Inst.grid(row=0, column=0, padx=10, pady=2, sticky=W)

instructions = "When one of the buttons on the is clicked, a circle\
 of the selected color appears in the canvas above. Red will result in a red circle. The color that is\
 selected will also appear in the output box below. This will track the various colors that\
 have been chosen in the past."
Instruct = Label(leftFrame, width=22, height=10, text=instructions, takefocus=0, wraplength=170, anchor=W, justify=LEFT, bg="#C8F9C4")
Instruct.grid(row=1, column=0, padx=10, pady=2)

imageEx = PhotoImage(file = 'image.png')
Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)


#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 600, bg="#C8F9C4", highlightthickness=2, highlightbackground="#111")
rightFrame.grid(row=0, column=1, padx=10, pady=2, sticky=N+S)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white', highlightthickness=1, highlightbackground="#333")
circleCanvas.grid(row=0, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200, bg="#C8F9C4")
btnFrame.grid(row=1, column=0, padx=10, pady=2)

colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0, highlightthickness=1, highlightbackground="#333")
colorLog.grid(row=2, column=0, padx=10, pady=2)

redBtn = Button(btnFrame, text="Red", command=redCircle, bg="#EC6E6E")
redBtn.grid(row=0, column=0, padx=10, pady=2)

yellowBtn = Button(btnFrame, text="Yellow", command=yelCircle, bg="#ECE86E")
yellowBtn.grid(row=0, column=1, padx=10, pady=2)

greenBtn = Button(btnFrame, text="Green", command=grnCircle, bg="#6EEC77")
greenBtn.grid(row=0, column=2, padx=10, pady=2)


mainloop()
