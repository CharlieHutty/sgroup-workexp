import datetime as dt
import startdate
from datetime import date
import enddate
import endtime

def StartTime():
    # For todays time
    datetoday = date.today()
    # For todays date
    timetoday = dt.datetime.today()
    print('The time is: ', timetoday.strftime('%H:%M'))
    # The format we want the time in
    timeformat = '%H%M'
    while True:
        # Allow the user to enter the time they would like to book the room
        timestart = input("What time would you like the booking to start? Enter in 24-hour format ")
        try:
            timestart = dt.datetime.strptime(timestart, timeformat)     # Checks to make sure that the data is in the correct format
        except ValueError:
            print("Incorrect format")
        else:
            timestart = timestart.strftime('%H%M')  # This takes off the unnecessary parts
            return timestart
