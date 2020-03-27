from layouts.LayoutManager import*
class Window:

    size = "2000x2000"
    counter = 1
    welcomPage = None
    newFrames = None
    num = 0

    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.welcomPage = Frame(parent,padx=50,pady=50)
        self.welcomPage.pack(padx=10,pady=10)
        self.LOM = LayoutManager()
        startButton = Button(self.welcomPage, text = "Start", command=lambda:self.start())
        startButton.pack()

    def handler(self):

        self.newFrames = Frame(self.root, height=2000, width=2000)
        self.newFrames.pack()
        self.LOM.getLay1(self.newFrames, self)


    def start(self):
        self.welcomPage.destroy()
        self.handler()
    # ---------------   -------------------------------------------------------

    def change(self):
        self.newFrames.destroy()
        self.newFrames2 = Frame(self.root, height=2000, width=2000)
        self.newFrames2.pack()
        self.LOM.getLay2(self.newFrames2, self)

    def changeAgain(self):
        self.newFrames2.destroy()
        self.newFrames3 = Frame(self.root, height=2000, width=2000)
        self.newFrames3.pack()
        self.LOM.getLay3(self.newFrames3, self)