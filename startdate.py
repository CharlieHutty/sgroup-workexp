import datetime as dt
from datetime import date

def startdate():
    while True:
        today = date.today()
        print("Today's date is: ", today.strftime('%d/%m/%Y'))
        # This is the date format in which we want the data entered in
        dateformat = '%d/%m/%Y'
        # Allow the user to input what date they would like to book the room
        datestart = input("What date would you like the room to be booked? Type Date dd/mm/yyyy: ")
        try:
            datestart = dt.datetime.strptime(datestart, dateformat) # Checks to see if the format matches
        except ValueError:
            print("Incorrect format")   # Tells the user that the format is wrong
            # Makes them try again
        else:
            if str(datestart) < str(today):
                print("Please enter a valid date")
            else:
                datestart = datestart.strftime('%d/%m/%Y')  # This takes off the unnecessary parts
                return datestart
                # Carries on the program if no errors are found
