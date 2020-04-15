from layouts.LayoutManager import*


class Window:

    size = 50
    font = "Helvetica"
    counter = 1
    welcomPage = None
    newFrames = None
    num = 0

    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.welcomPage = Frame(parent,padx=50,pady=50)
        self.welcomPage.pack(padx=10,pady=10)
        startButton = Button(self.welcomPage, text = "Start", font=(self.font, self.size), command=lambda:self.start())
        startButton.pack()
        print "run"



    def handler(self):

        self.LOM = LayoutManager()
        self.newFrames = Frame(self.root, height=100,background="red", width=100)
        self.newFrames.pack( padx=20, pady=200)
        self.LOM.getLay1(self.newFrames, self)


    def start(self):
        self.welcomPage.destroy()
        self.handler()
    # ---------------   -------------------------------------------------------

    def change(self):
        self.newFrames.destroy()
        self.newFrames2 = Frame(self.root, height=self.height, width=self.width)
        self.newFrames2.pack()
        self.LOM.getLay2(self.newFrames2, self,self.width,self.height)

    def changeAgain(self):
        self.newFrames2.destroy()
        self.newFrames3 = Frame(self.root,  height=100,background="red", width=100)
        self.newFrames3.pack( padx=20, pady=400)
        self.LOM.getLay3(self.newFrames3, self)


    def end(self):
        self.newFrames3.destroy()
