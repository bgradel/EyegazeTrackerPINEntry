from Layout1 import*
from Layout2 import*
from Layout3 import*
from Buttons import*

class LayoutManager:

    def getLay1(self, root, obj):
        but = Buttons(obj,1)
        buttons = but.creatButtons(root)
        l1 = Layout1(buttons)

    def getLay2(self, root, obj):
        button2 = Buttons(obj,2)
        buttons = button2.creatButtons(root)
        l2 = Layout2(buttons)

    def getLay3(self, root, obj):
        button3 = Buttons(obj,3)
        buttons = button3.creatButtons(root)
        l3 = Layout3(buttons)
