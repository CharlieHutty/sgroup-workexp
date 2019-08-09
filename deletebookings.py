import csv

def DeleteBookings():



    with open('ExistingBookings.csv', 'r') as ExistingBookings:

        readCSV = csv.reader(ExistingBookings, delimiter=',')

        # rowtodelete = int(input("Enter the number of the row you want to delete: "))

        i = 1
        for row in ExistingBookings:
            # print(i, '\n', row)
            # i = i + 1
            name = row[0]
            roomtobook = row[1]
            startdate = row[2]
            enddate = row[3]
            starttime = row[4]
            endtime = row[5]

            rows =[str(name), str(roomtobook), str(startdate), str(enddate), str(starttime), str(endtime)]

            print(rows)



