from Tkinter import *
root=Tk()
b=Button(root,justify = LEFT)
photo=PhotoImage(file="layouts/pix.gif")
b.config(image=photo,width="10",height="10")
b.pack(side=LEFT)
root.mainloop()