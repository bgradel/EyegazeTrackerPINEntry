from Layout1 import*
from Layout2 import*
from Layout3 import*
from Buttons import*
from TimeCount import*

class LayoutManager:

    def __init__(self):
        self.timer = TimeCounts.getInstance()
        self.timer.writeToFile("Layout1,")

    def getLay1(self, root, obj):
        but = Buttons(obj,1, self.timer)
        buttons = but.creatButtons(root)
        l1 = Layout1(buttons)

    def getLay2(self, root, obj, width, height):
        button2 = Buttons(obj,2, self.timer)
        buttons = button2.creatButtons(root)
        l2 = Layout2(buttons,width, height)


    def getLay3(self, root, obj):
        button3 = Buttons(obj,3, self.timer)
        buttons = button3.creatButtons(root)
        l3 = Layout3(buttons)
