import datetime as dt

def callPyTime():
    time= dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(time)
    return time