import username
import roomtobook
import enddate
import startdate
import starttime
import endtime
import csv

def FileHandle():

    # Open the csv
    with open('ExistingBookings.csv', 'a') as ExistingBookings:
        ExistingBookings = csv.writer(ExistingBookings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Writes the users input to the CSV
        ExistingBookings.writerow([username, roomtobook, datestart, dateend, timestart, timeend])

        print(username, roomtobook, datestart, dateend, timestart, timeend)
