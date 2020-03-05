from layouts.LayoutManager import*
from Buttons import*

class Window:
    root = Tk()
    size = "2000x2000"
    counter = None

    frame1 = LabelFrame(root)
    frame2 = LabelFrame(root)
    frame3 = LabelFrame(root)

    frames = [frame1,frame2,frame3]

    screenHeight = root.winfo_screenheight()
    screenWidth = root.winfo_screenwidth()

    root.geometry(size)


    button = Buttons(root)
    button.creatButtons()
    buttonList = button.buttonList

    LM = LayoutManager(frames,buttonList)
    LM.getLay2()

    #LM.getLay1()

    root.mainloop()

