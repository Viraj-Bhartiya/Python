from time import sleep

def timer (seconds) :
    while seconds:
        min , sec = divmod(seconds,60)
        count = '{:02d}:{:02d}'.format(min,sec)
        print(count , end='\r')
        sleep(1)
        seconds-=1
timer(30)
print("time's up")