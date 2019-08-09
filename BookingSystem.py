# Meeting Room Booking system
# Charlie Hutty
# 7/8/19

# import modules
import datetime as dt
import csv
import username
import roomtobook
import enddate
import startdate
import starttime
import endtime
import deletebookings


def CheckBooking():
    # Open the csv file
    with open('ExistingBookings.csv') as ExistingBookings:
        readCSV = csv.reader(ExistingBookings, delimiter=',')
        bookedrooms = []
        for row in readCSV:
            bookedrooms = row[1]
            startdate = row[2]
            starttime = row[4]


        if str(roomtobook) == str(bookedrooms) and str(datestart) == str(startdate) and str(timestart) == str(starttime):
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

        print('\n Name: ', username, '\n', 'Room Booked: ', roomtobook, '\n', 'Start Date: ', datestart, '\n', 'End Date: ', dateend, '\n', 'Start Time: ', timestart, '\n', 'End Time: ', timeend)

def DeleteBookings():
    with open('ExistingBookings.csv') as ExistingBookings:
        readCSV = csv.reader(ExistingBookings, delimiter=',')
        for row in ExistingBookings:
            print(row)
    # Open and read the csv
    print("The top row is 1")
    rowtodelete = int(input("Please enter the number row you want to delete"))
    rowtodelete = row[rowtodelete]

    with open('ExistingBookings.csv', 'w') as ExistingBookings:
        ExistingBookings = csv.writer(ExistingBookings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Writes the users input to the CSV
        ExistingBookings.writerow([rowtodelete, " "])



if __name__ == "__main__":
    username = username.UserName()
    roomtobook = roomtobook.RoomToBook()
    datestart = startdate.startdate()
    dateend = startdate.enddate()
    timestart = starttime.StartTime()
    timeend = endtime.endtime()
    CheckBooking()
    # deletebookings.DeleteBookings()






