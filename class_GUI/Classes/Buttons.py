from Tkinter import*
from Pin import *


class Buttons:
    buttonList = []
    root = None
    size = 60
    padding = 5
    font = "Courier"

    def __init__(self,root):
        self.root = root

    def creatButtons(self):
        for i in range(10):
            self.buttonList.append(Button(self.root, text=str(i), borderwidth=5, font=(self.font, self.size),
                            command=lambda a=i: self.click(a)))


    def click(self,num):
        Pin.append(num)



    #creatButtons()