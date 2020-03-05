from Tkinter import*
from Window import*
from math import*
import math



class Layout2:
    win_x = 400
    win_y = 400
    length = 500
    xx = int(length*math.sin((15*math.pi)/180))
    yy = int(length*math.cos((15*math.pi)/180))
    hh = int(length*math.cos((45*math.pi)/180))
    root = None
    buttonList = []
    buttonCoor = [[500+hh,500+hh],[500+xx,500+yy],[500-xx,500+yy],[500-hh,500+hh],[500-yy,500-xx],[500-yy,500+xx],[500-hh,500-hh],[500-xx,500-yy],[500+xx,500-yy],[500+hh,500-hh]]
    degree = 15


    def __init__(self,root,bList):
        self.root = root
        self.buttonList = bList


    # use the x and y to place button
    def placeButton(self):
        for i in range(10):
            self.buttonList[i].place(x=self.buttonCoor[i][0],y=self.buttonCoor[i][1])
            print self.buttonCoor[i][0]


    # find the exact x and y for button placement
    # a list of xy is stored in a list