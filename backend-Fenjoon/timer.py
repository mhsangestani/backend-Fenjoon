import time


def countdown(t):
    # a while loop runs until time becomes 0
    while t:
        # calculate the number of minutes and seconds
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        # the next line printed will overwrite the previous one
        print(timer, end="\r")
        # makes the code wait for one sec
        time.sleep(1)
        t -= 1
        

countdown(180)