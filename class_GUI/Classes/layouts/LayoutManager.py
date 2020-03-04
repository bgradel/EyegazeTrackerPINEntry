from Layout1 import*
from Layout2 import*
from Layout3 import*


class LayoutManager:

    frames = []
    buttonList = []

    def __init__(self,frames,buttonList):
        self.frames = frames
        self.buttonList = buttonList

    def getLay1(self):
        l1 = Layout1(self.frames[0], self.buttonList)
        l1.placeButton()
        self.frames[0].destroy()

    def getLay2(self):
        l2 = Layout2(self.frames[1], self.buttonList)
        l2.placeButton()

    def getLay3(self):
        l3 = Layout3(self.frames[2], self.buttonList)
        l3.placeButton()

    @classmethod
    def changeLayout(cls):
        cls.getLay3()