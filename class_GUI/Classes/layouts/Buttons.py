from Tkinter import*
from Pin import *
from Classes.Window import *


class Buttons:
    size = 60
    padding = 5
    font = "Courier"

    def __init__(self,obj, num):
        self.obj = obj
        self.p = num

    def creatButtons(self,root):
        buttonList = []
        for i in range(10):
            buttonList.append(Button(root, text=str(i), borderwidth=5, font=(self.font, self.size),
                            command=lambda a=i: self.click(a)))
            print 1
        return buttonList


    def click(self,num):
        bol = Pin.append(num)
        if bol == True:
            if self.p == 1:
                self.obj.change()
                print "change"
            else:
                print "change again"
                self.obj.changeAgain()
        else:
            print "False"


    #creatButtons()