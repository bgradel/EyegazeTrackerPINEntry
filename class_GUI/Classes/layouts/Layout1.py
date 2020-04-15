class Layout1:
    root = None
    buttonList = []
    k = 1

    def __init__(self,bList):
        self.buttonList = bList
        self.placeButton()

    def placeButton(self):
        for i in range(3):
            for j in range(3):
                self.buttonList[self.k].grid(row=i, column=j,padx=5,pady=5)
                self.k += 1
        self.buttonList[0].grid(row=3,column=1,padx=5,pady=5)
