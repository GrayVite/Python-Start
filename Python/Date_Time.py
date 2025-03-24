import datetime
import time
import pygame

# It will use our computer's clock
def basics():
    date = datetime.date(2025, 2, 20) # (year, numerical month, date)
    print(date)

    today =  datetime.date.today()
    print(today) # Returns in year, month, date

    time = datetime.time(12, 30, 0) # (hrs, mins, secs)
    print(time)

    # We are accessing the datetime class within the datetime module 
    time_now = datetime.datetime.now() # It returns the time along the date
    print(time_now)

    # You can find the format specifiers in the online documentation for the module
    # H->hrs, M->mins, S->secs, m->month, d->day, Y->year
    time_now = time_now.strftime("%H:%M:%S %d/%m/%Y")
    print(time_now)

def exercise():
    target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1) # (year, month, date, hour, min, sec)
    current_datetime = datetime.datetime.now()

    if target_datetime < current_datetime:
        print(f"Target date has passed")
    else:
        print(f"Target date has not passed")

