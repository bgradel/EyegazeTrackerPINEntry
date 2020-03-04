class Layout3:

    root = None
    buttonList = []
    counter = 1

    def __init__(self,root,bList):
        self.root = root
        self.buttonList = bList

    def placeButton(self):
        for i in range(2):
            for j in range(5):
                if self.counter <= 9:
                    self.buttonList[self.counter].grid(row=i, column=j)
                    self.counter += 1
                else:
                    self.buttonList[0].grid(row=i, column=j)