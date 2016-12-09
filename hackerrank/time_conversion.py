import sys


time = "12:05:45PM".strip().split(":")

if "PM" in time[-1]:
    if ( int(time[0]) <= 11):
        time[0] = int(time[0])+ 12
    elif int(time[0]) == 12:
        time[0] = "12"
    else:
        time[0] = "00"

    time[0] = str(time[0])
    time[-1] = time[-1].strip("PM")

if "AM" in time[-1]:
    if ( int(time[0]) == 12):
        time[0] = "00"

    time[-1] = time[-1].strip("AM")

print(":".join(time))
