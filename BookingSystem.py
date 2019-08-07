# Meeting Room Booking system
# Charlie Hutty
# 7/8/19

# import modules
import datetime as dt
import csv


def UserName():
    while True:
        global username # Gloabal variable that can be passed through the functions
        #Allow the user to enter their name
        username = str(input("Enter your name: "))
        if type(username) is not str:
            print("That is not a name")
            print("Try again")
            username = str(input("Enter your name: "))
        else:
            break


def RoomToBook():
    while True:
        global roomtobook # Gloabl variable, can be accessed throughout the program
        # Allow the user to enter the room they would like to book
        roomtobook = int(input("Enter the number of room you would like to book (1-4): ")) # Gets the users input
        if roomtobook < 1 or roomtobook > 4: # Makes sure that the users input is within the boundaries
            print("Please enter a number between 1 and 4") # Makes the user keep repeating the line until they are within the boundaries
        else:
            break # Breaks out of the loop when the conditions are met



def DateToBook():
    global datestart
    global dateend
    while True:
        # This is the date format in which we want the data entered in
        dateformat = '%d/%m/%Y'
        # Allow the user to input what date they would like to book the room
        datestart = input("What date would you like the room to be booked? Type Date dd/mm/yyyy: ")
        try:
            datestart = dt.datetime.strptime(datestart, dateformat) # Checks to see if the format matches
        except ValueError:
            print(("Incorrect format")) # Tells the user that the format is wrong
            # Makes them try again
        else:
            datestart = datestart.strftime('%d/%m/%Y')# This takes off the unnecessary parts
            break # Carries on the program if no errors are found

    while True:
        # Allow the user to enter the date the booking will end
        dateend = input("What date would you like the booking to end? Type Data dd/mm/yyyy: ")
        try:
            dateend = dt.datetime.strptime(dateend, dateformat)
        except ValueError:
            print("Incorrect format")
        else:
            dateend = dateend.strftime('%d/%m/%Y')# This takes off the unnecessary parts
            break

def TimeToBook():
    global timestart
    global timeend
    # The format we want the time in
    timeformat = '%H%M'

    while True:
        # Allow the user to enter the time they would like to book the room
        timestart = input("What time would you like the booking to start? Enter in 24-hour format ")
        try:
            timestart = dt.datetime.strptime(timestart, timeformat) # Checks to make sure that the data is in the correct format
        except ValueError:
            print("Incorrect format")
        else:
            timestart = timestart.strftime('%H%M')# This takes off the unnecessary parts
            break
    # For the end time of the meeting
    while True:
        # Allow the user to enter the time they would like the booking to end
        timeend = input("What time would you like the booking to end? ")
        try:
            timeend = dt.datetime.strptime(timeend, timeformat)
        except ValueError:
            print("Incorrect format")
        else:
            timeend = timeend.strftime('%H%M') # This takes off the unnecessary parts
            break


def FileHandle():
    # Open the text file
    f = open("ExsistingBookings.txt", "a+") # Tells the program that were going to be appending, not to overwrite the file
    f.write("Name: "+ username+"\n"+"Room: "+ str(roomtobook)+"\n"+"Start Date: "+ str(datestart)+"\n"+"End Date: "+str(dateend)+"\n"+"Start Time: "+str(timestart)+"\n"+"End Time: "+str(timeend)+"\n\n" ) # This is the format that the infomation will be appended in
    f.close() # Closes the text file

    ##

    with open('Bookings.csv', 'w', newline='') as csvfile:
        # https://docs.python.org/3.2/library/csv.html?highlight=csv#csv



if __name__ == "__main__":
    UserName()
    RoomToBook()
    DateToBook()
    TimeToBook()
    FileHandle()






