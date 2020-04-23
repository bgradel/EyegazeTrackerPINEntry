from Tkinter import*
from Pin import *
import TimeCount
from Classes.Window import *


class Buttons:
    size = 170
    bsize = size-15
    padding = 0
    font = "Time New Roman"


    def __init__(self,obj, num, timer):
        self.obj = obj
        self.p = num
        self.timer = timer
        self.photo = PhotoImage(file= "layouts/pix.gif")

    def creatButtons(self,root):
        buttonList = []

        for i in range(10):
            b = Button(root, image = self.photo,text = str(i), width = self.size, height = self.size, compound = CENTER, borderwidth=2, relief = SOLID, font=(self.font, self.bsize),
                            command=lambda a=i: self.click(a))
            buttonList.append(b)
        return buttonList


    def click(self,num):
        self.timer.get_press_time()
        bol = Pin.append(num)
        if bol == True:
            if self.p == 1:
                self.obj.change()
                print "change"
                self.timer.get_window_time()
                self.timer.writeToFile("Layout2,")
            elif self.p == 2:
                print "change again"
                self.timer.get_window_time()
                self.obj.changeAgain()
                self.timer.writeToFile("Layout3,")
            else:
                self.timer.get_window_time()
                self.timer.get_best()
                self.timer.writeToFile(self.timer.getDuration())
                self.obj.end()
                exit()
        elif bol == False:
            if self.p == 1:
                self.timer.get_window_time()
                self.timer.writeToFile("Layout1,")
                print "olsdasfgsagsdgsd"
            elif self.p == 2:
                self.timer.get_window_time()
                self.timer.writeToFile("Layout2,")
            else:
                self.timer.get_window_time()
                self.timer.writeToFile("Layout3,")
    #creatButtons()