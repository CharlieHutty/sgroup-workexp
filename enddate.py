import datetime as dt
from datetime import date
import startdate

def enddate():
    while True:
        dateformat = '%d/%m/%Y'
        # Allow the user to enter the date the booking will end
        dateend = input("What date would you like the booking to end? Type Data dd/mm/yyyy: ")
        try:
            dateend = dt.datetime.strptime(dateend, dateformat)
        except ValueError:
            print("Incorrect format")
        else:
            if str(dateend) >= str(datestart):
                print("Please enter a valid date")  # Makes sure that the user inputs a valid date
            else:
                dateend = dateend.strftime('%d/%m/%Y')  # This takes off the unnecessary parts
                return dateend
