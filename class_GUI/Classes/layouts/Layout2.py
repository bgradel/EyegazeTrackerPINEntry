from Tkinter import*
from Window import*
from math import*
import math



class Layout2:



    def __init__(self, bList,width, height):
        self.width = width/2
        self.height = height//2.5
        print self.width,self.height
        self.buttonList = bList
        self.calcu()
        self.placeButton()

    def calcu(self):
        win_x = self.width
        win_y = self.height
        length = 400
        error = 22

        xx = int(length * math.sin((15 * math.pi) / 180))
        yy = int(length * math.cos((15 * math.pi) / 180))
        hh = int(length * math.cos((45 * math.pi) / 180))
        self.buttonCoor = [[win_x + hh - error, win_y + hh - error], [win_x + xx - error, win_y + yy - error],
                      [win_x - xx, win_y + yy - error], [win_x - hh, win_y+ hh - error], [win_x - yy, win_y - xx],
                      [win_x - yy, win_y + xx - error], [win_x - hh, win_y - hh], [win_x - xx, win_y - yy],
                      [win_x + xx - error, win_y - yy], [win_x + hh - error, win_y - hh]]
        degree = 15
    # use the x and y to place Buttons.py
    def placeButton(self):
        for i in range(10):
            self.buttonList[i].place(x=self.buttonCoor[i][0],y=self.buttonCoor[i][1])


    # find the exact x and y for Buttons.py placement
    # a list of xy is stored in a list