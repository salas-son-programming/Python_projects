# Simple Alarm Clock
# o User sets a time.
# o Program checks current time in a loop.
# o When matched, plays a sound or prints “Time’s up!”

import datetime
import time
#time.sleep(1)
minute=int(input("enter the minute: "))
hour=int(input("enter the hour: "))
scope=input("AM or PM?: ").upper()



while True:
    time.sleep(1)
    x = datetime.datetime.now()
    print(f"{x.strftime("%B")} {x.strftime("%d")}, {x.strftime("%Y")}")
    print(f"{x.strftime("%I")}:{x.strftime("%M")} {x.strftime("%p")}")
    if x.strftime("%I") == hour and x.strftime("%M") == minute and x.strftime("%p") == scope:
        print("times up")

