import Window
from Tkinter import *
import threading

class Luncher:
    if __name__ == "__main__":
        root = Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        size = str(width) + 'x' + str(height)
        root.geometry(size)
        app = Window.Window(root)
        root.mainloop()
