class Layout3:

    root = None
    buttonList = []
    counter = 1

    def __init__(self,bList):
        self.buttonList = bList
        self.placeButton()
        print "L3"

    def placeButton(self):
        for i in range(2):
            for j in range(5):
                if self.counter <= 9:
                    self.buttonList[self.counter].grid(row=i, column=j,padx=1,pady=1)
                    self.counter += 1
                else:
                    self.buttonList[0].grid(row=i, column=j,padx=1,pady=1)