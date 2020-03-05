from Tkinter import*

root = Tk()



root.geometry("1000x1000")

frame = LabelFrame(root)
frame.place(x=10,y=10)
b = Button(frame,text="sdasdasd",command=lambda: dell(frame))
b.pack()

#frame.destroy()

frame2 = LabelFrame(root)
frame2.place(x=10,y=10)
a = Button(frame2,text="sdasdasd",command=lambda: dell(frame))
a.pack()

def dell(frame):
    if (counter / 2) == 0:
        frame.place_forget()
        counter = counter + 1
    else:
        frame.place
        frame2.place_forget()

root.mainloop()