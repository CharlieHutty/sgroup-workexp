import datetime as dt
import starttime
import startdate
import enddate

def endtime():
    # For todays date
    today = dt.datetime.today()
    print('The time is: ', today.strftime('%H%M'))
    # The format we want the time in
    timeformat = '%H%M'
    # For the end time of the meeting
    while True:
        # Allow the user to enter the time they would like the booking to end
        timeend = input("What time would you like the booking to end? ")
        try:
            timeend = dt.datetime.strptime(timeend, timeformat)
        except ValueError:
            print("Incorrect format")
        else:
            if str(enddate) < str(st):
                print("Enter a valid date")
            else:
                timeend = timeend.strftime('%H%M')  # This takes off the unnecessary parts
                return timeend
