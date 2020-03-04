#! python
import pyautogui, sys, time
file = open('test.txt','w')
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        file.writelines(positionStr + " "+  str(time.clock()) + '\n' )
        #file.writelines( '\b' * (len(positionStr) + 2))
        sys.stdout.flush()
except KeyboardInterrupt:
    file.write( '\n')
    file.close()