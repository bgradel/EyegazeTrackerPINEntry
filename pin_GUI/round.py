from Tkinter import*
import math
root = Tk()

# window size
win_x = 400
win_y = 400

size = "500x500"
root.geometry(size)

screenHeight = root.winfo_screenheight()
screenWidth = root.winfo_screenwidth()

centerPoint = [win_x//2,win_y//2]

print(screenHeight)

# creating a Label Widget
#e = Entry(root, width = 10, borderwidth=5,font=30)
#e.grid(row=0,column=1)

e = Entry(root, width = 10, borderwidth=5,font=30)
e.place(x=centerPoint[0],y=centerPoint[1])

def click(num):
    e.insert(len(e.get()),num)

def callback():
    input = e.get()
    if input == "0404":
        e.delete(0, END)
        e.insert(0, "your in!")
    else:
        e.delete(0, END)
        e.insert(0, "please try again")

def clear():
    e.delete(0, END)

def getCoordinate(length):
    return length/2, (length/2)*math.sqrt(3)


def roundButton():
    x,y=getCoordinate(200)
    print(y)
    actionBtn = Button(root, text="1", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(1)).place(x=centerPoint[0], y=0)
    actionBtn = Button(root, text="2", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(2)).place(x=centerPoint[0]+x, y=centerPoint[1]-y)
    actionBtn = Button(root, text="3", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(3)).place(x=centerPoint[0]+y, y=centerPoint[1]-x)
    actionBtn = Button(root, text="4", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(4)).place(x=centerPoint[0]+centerPoint[0], y=centerPoint[1])
    actionBtn = Button(root, text="5", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(5)).place(x=centerPoint[0]+y, y=centerPoint[1]+x)
    actionBtn = Button(root, text="6", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(6)).place(x=centerPoint[0]+x, y=centerPoint[1]+y)
    actionBtn = Button(root, text="7", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(7)).place(x=centerPoint[0], y=win_y)
    actionBtn = Button(root, text="8", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(8)).place(x=centerPoint[0]-x, y=centerPoint[1]+y)
    actionBtn = Button(root, text="9", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(9)).place(x=centerPoint[0]-y, y=centerPoint[1]+x)
    actionBtn = Button(root, text="0", width=5, height=2,borderwidth=5, font=("Courier",14), command=lambda:click(10)).place(x=0, y=centerPoint[1])


roundButton()

root.mainloop()