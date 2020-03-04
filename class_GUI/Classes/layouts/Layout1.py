class Layout1:
    root = None
    buttonList = []
    k = 1

    def __init__(self,root,bList):
        self.root = root
        self.buttonList = bList

    def placeButton(self):

        for i in range(3):
            for j in range(3):
                self.buttonList[self.k].grid(row=i, column=j)
                self.k += 1
                print 2
        self.buttonList[0].grid(row=3,column=1)
