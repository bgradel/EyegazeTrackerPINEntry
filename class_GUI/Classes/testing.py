from Tkinter import *

root = Tk()
root.title("main frame")

frame = Frame(root, height = 100, width = 100)
frame.pack(padx=5,pady=5)



b = Button(frame,text="yes!",command=lambda:handler(frame, 0))
b.place(x=33,y=44)
print 44

i = 1

def handler(frames):
    frames.destroy()
    frame2 = LabelFrame(root, padx=50, pady=50)

    frame2.pack(padx=10,pady=10)
    c = Button(frame2,text=str(i), command=lambda:handler(frame2))
    c.grid(row=0,column=0)

def screen2(frame2):
    frame2.destroy()
    frame3 = LabelFrame(root, padx=50, pady=50)
    frame3.pack(padx=10, pady=10)

    c = Button(frame3, text="second",command=lambda:screen3(frame3))
    c.grid(row=0, column=0)

def screen3(frame3):
    frame3.destroy()
    frame4 = LabelFrame(root, padx=50, pady=50)
    frame4.pack(padx=10, pady=10)

    c = Button(frame4, text="third")
    c.grid(row=0, column=0)

root.mainloop()