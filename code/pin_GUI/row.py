from Tkinter import*

root = Tk()

# creating a Label Widget
e = Entry(root, width = 10, borderwidth=5,font=30)
e.grid(row=0,column=1)

photo = PhotoImage(file="unnamed.gif")
photo1 = photo.subsample(3,3)

a = []
num = [1,2,3,4,5,6,7,8,9,0]

buttonSize = 50

def click(num):
    e.insert(len(e.get()), num)
    a.append(num)

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

number = 0

for i in range(2):
    for j in range(5):
        button = Button(root,text=str(num[number]), borderwidth=5, font=("Courier",44), command= lambda a = number: click(num[a]))
        button.grid(row=i+1, column=j)

        number += 1


enter = Button(root,text="Enter",borderwidth=5, font=("Courier",14), command=callback)
enter.grid(row=4, column = 2)

delete = Button(root,text="delete", borderwidth=5, font=("Courier",14), command=clear)
delete.grid(row=4, column = 0)

root.mainloop()

