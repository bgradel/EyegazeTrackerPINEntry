import timeit
from Pin import*

# this is a singleton class

class TimeCounts:

    _instance = None
    counter = 0

    # this method is used for other class to access this instance, there is only one timer.
    @staticmethod
    def getInstance():
        if TimeCounts._instance == None:
            TimeCounts()
        return TimeCounts._instance

    def __init__(self):
        if TimeCounts._instance != None:
            raise Exception("This class is a singleton of TimeCounts")
        else:
            TimeCounts._instance = self
            self.file = open("data.txt", "w")
            self.file.write("layoutName,1_deltaSinceLastButtonPressed(sec),2_deltaSinceLastButtonPressed(sec),3_deltaSinceLastButtonPressed(sec),4_deltaSinceLastButtonPressed(sec),WindowDurationPerEnterd(sec),Correct/InccorectOfPinEntry, PINEnteredInput\n")
            self.start_time = timeit.default_timer()
            self.buttonPress = self.start_time
            self.windowChange = self.start_time
            self.lis = []

    def get_press_time(self):
        end_time = timeit.default_timer() - self.buttonPress
        self.buttonPress = timeit.default_timer()
        info = str(end_time) + ","
        self.writeToFile(info)
        return end_time

    def get_window_time(self):
        end_time = timeit.default_timer() - self.windowChange
        self.lis.append(end_time)
        self.windowChange = timeit.default_timer()
        pin = Pin.getEntry()
        boo = Pin.checkPins(pin)
        if boo == True:
            info = str(end_time) +","+ "1" +","+ pin + "\n"
        else:
            info = str(end_time) + "," + "0" + "," + pin + "\n"
        self.writeToFile(info)
        return end_time

    def next_line(self):
        self.writeToFile("\n")

    def get_best(self):
        print self.lis
        fastest = 999
        index = 0
        for i in range(len(self.lis)):
            if self.lis[i] < fastest:
                fastest = self.lis[i]
                index = i
        print "layout " + str(index+1) + " have the best result with a time of " + str(fastest)

    def getDuration(self):
        return "ProgramDuration: " + str(timeit.default_timer()-self.start_time)

    def writeToFile(self,info):
        self.file.write(str(info))
