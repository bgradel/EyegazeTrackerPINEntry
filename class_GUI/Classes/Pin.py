import random
from layouts.LayoutManager import*
from Tkinter import *
from Window import *

class Pin:
    pin = "0404"
    entry = ""
    root = None

    @classmethod
    def getEntry(cls):
        value = cls.entry
        cls.entry = ""
        return value

    @classmethod
    def checkPins(cls, pin):
        return cls.pin == pin

    @classmethod
    def creatRandomPin(cls):
        cls.pin = str(random.random()*1000)

    @classmethod
    def setPin(cls,pin):
        cls.pin = pin

    @classmethod
    def append(cls,num):
        cls.entry = cls.entry + str(num)
        return cls.checkPin()

    @classmethod
    def checkPin(cls):
        print len(cls.entry)
        print cls.entry
        if len(cls.entry) == 4:
            if cls.entry == cls.pin:
                print "you got it!"
                return True
            else:
                print "try again"
                return False
        else:
            return
