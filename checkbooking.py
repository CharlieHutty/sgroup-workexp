
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
            BookingSystem.FileHandle()    # Runs the function to put the user details into the csv

