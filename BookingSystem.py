# Meeting Room Booking system
# Charlie Hutty
# 7/8/19

# import modules
import datetime as dt
from datetime import date
import csv

# Menu
def menu():

    global userchoice
    print("1. Create booking")
    print("2. Delete booking")
    print("3. View Booking")
    print("4. Quit", '\n')
    userchoice = input("What would you like to do: ")

def UserName():
    while True:
        global username     # Gloabal variable that can be passed through the functions
        # Allow the user to enter their name
        username = input("Enter your name: ").lower()
        if username.isalpha():
            break
        else:
            print("That is not a name")
            print("Try again")

def RoomToBook():
    while True:
        global roomtobook   # Gloabl variable, can be accessed throughout the program
        # Allow the user to enter the room they would like to book
        roomtobook = int(input("Enter the number of room you would like to book (1-4): "))  # Gets the users input
        if roomtobook < 1 or roomtobook > 4:    # Makes sure that the users input is within the boundaries
            print("Please enter a number between 1 and 4")  # Makes the user keep repeating the line until they are within the boundaries
        else:
            break   # Breaks out of the loop when the conditions are met

def DateToBook():
    global datestart
    global dateend
    global datestart_str
    today = date.today()
    print("Today's date is: ", today.strftime('%d/%m/%Y'))
    while True:
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
            if datestart.date() < today:
                print("Invalid date")
            else:
                datestart_str = datestart.strftime('%d/%m/%Y')  # This takes off the unnecessary parts
                break # Carries on the program if no errors are found
    while True:
        # Allow the user to enter the date the booking will end
        dateend = input("What date would you like the booking to end? Type Data dd/mm/yyyy: ")
        try:
            dateend = dt.datetime.strptime(dateend, dateformat)
        except ValueError:
            print("Incorrect format")
        else:
            if datestart.date() > dateend.date():   # Throws error
                print("Enter a valid date")
            else:
                dateend = dateend.strftime('%d/%m/%Y')  # This takes off the unnecessary parts
                break

def TimeToBook():
    global timestart
    global timeend
    global timestart_str
    today = date.today()
    # The format we want the time in
    timeformat = '%H%M'
    # The current time
    timetoday = dt.datetime.today()
    print("The time now is: ", timetoday.strftime('%H%M'))
    while True:
        # Allow the user to enter the time they would like to book the room
        timestart = input("What time would you like the booking to start? Enter in 24-hour format ")
        try:
            timestart = dt.datetime.strptime(timestart, timeformat)     # Checks to make sure that the data is in the correct format
        except ValueError:
            print("Incorrect format")
        else:
            if daetstart.time() < timetoday.time():
                print("Invalid time")
            else:
                timestart_str = timestart.strftime('%H%M')  # This takes off the unnecessary parts
                break
    # For the end time of the meeting
    while True:
        # Allow the user to enter the time they would like to book the room
        timeend = input("What time would you like the booking to end? Enter in 24-hour format ")
        try:
            timeend = dt.datetime.strptime(timeend, timeformat)     # Checks to make sure that the data is in the correct format
        except ValueError:
            print("Incorrect format")
        else:
            if datestart_str == dateend:
                if timeend.time() < timestart.time():
                    print("Enter a valid time")
                else:
                    break
            else:
                timeend = timeend.strftime('%H%M')  # This takes off the unnecessary parts
                break

def CheckBooking():
    # Open the csv file
    with open('ExistingBookings.csv') as ExistingBookings:
        readCSV = csv.reader(ExistingBookings, delimiter=',')
        bookedrooms = []
        for row in readCSV:
            bookedrooms = row[1]
            startdate = row[2]
            enddate = row[3]
            starttime = row[4]
            endtime = row[5]

        if str(roomtobook) == str(bookedrooms) and str(datestart_str) <= str(dateend) and str(starttime) <= str(endtime):
            print("Room already booked")
        else:
            print("Successful")     # Outputs to the user that their booking has been successful
            FileHandle()    # Runs the function to put the user details into the csv

def FileHandle():
    # Open the csv
    with open('ExistingBookings.csv', 'a') as ExistingBookings:
        ExistingBookings = csv.writer(ExistingBookings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Writes the users input to the CSV
        ExistingBookings.writerow([username, roomtobook, datestart, dateend, timestart, timeend])

        # delta = (timeend - timestart)

        print('\n Name: ', username, '\n', 'Room Booked: ', roomtobook, '\n', 'Start Date: ', datestart_str, '\n', 'End Date: ', dateend, '\n', 'Start Time: ', timestart_str, '\n', 'End Time: ', timeend, '\n')
        # print("The meeting is ", delta, "mins long")

def DeleteBookings():
    username = input("What is your name: ")
    username = username.lower()
    # Open the csv file
    with open('ExistingBookings.csv') as csvfile:
        reader = csv.reader(csvfile)
        i = 1
        for row in reader:
            name = str(row[0])
            roomtobook = str(row[1])
            datestart_str = str(row[2])
            enddate = str(row[3])
            timetsart_str = str(row[4])
            endtime = str(row[5])
            if username == name:
                print('\n', 'Meeting:', i, '\n', "Room: ", roomtobook, '\n', "Start Date: ", datestart_str, '\n', "End date: ", enddate, '\n', "Start time: ", timetsart_str, '\n', "End time: ", endtime, '\n')
                i = i + 1
        meetingtodelete = input("What is the number of the meeting you would like to delete: ")
        if meetingtodelete == i:
            csv.writer(row[i])

def viewbookings():
    username = input("What is your name: ")
    username = username.lower()
    # Open the csv file
    with open('ExistingBookings.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = str(row[0])
            roomtobook = str(row[1])
            datestart_str = str(row[2])
            enddate = str(row[3])
            timetsart_str = str(row[4])
            endtime = str(row[5])
            if name == username:
                print('\n', "Room: ", roomtobook, '\n', "Start Date: ", datestart_str, '\n', "End date: ", enddate, '\n', "Start time: ", timetsart_str, '\n', "End time: ", endtime, '\n')

if __name__ == "__main__":
    while True:
        menu()
        if userchoice == '1':
            UserName()
            RoomToBook()
            DateToBook()
            TimeToBook()
            CheckBooking()
        elif userchoice == '2':
            DeleteBookings()
        elif userchoice == '3':
            viewbookings()
        else:
            break






