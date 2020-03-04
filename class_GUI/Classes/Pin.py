import random
from layouts.LayoutManager import*
from Tkinter import *

class Pin:
    pin = "0404"
    entry = ""

    @classmethod
    def checkPin(cls, pin):
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
        cls.checkPin()

    @classmethod
    def checkPin(cls):
        print len(cls.entry)
        print cls.entry
        if len(cls.entry) == 4:
            if cls.entry == cls.pin:
                cls.entry = ""
            else:
                cls.entry = ""
                return False
        else:
            return
