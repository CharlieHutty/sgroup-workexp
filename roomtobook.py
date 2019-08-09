
def RoomToBook():
    while True:
        # Allow the user to enter the room they would like to book
        roomtobook = int(input("Enter the number of room you would like to book (1-4): "))  # Gets the users input
        if roomtobook < 1 or roomtobook > 4:    # Makes sure that the users input is within the boundaries
            print("Please enter a number between 1 and 4")  # Makes the user keep repeating the line until they are within the boundaries
        else:
            return roomtobook

