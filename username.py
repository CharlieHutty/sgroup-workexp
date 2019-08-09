def UserName():
    while True:
        # Allow the user to enter their name
        username = input("Enter your name: ").lower()
        if username.isalpha():
            return username
        else:
            print("That is not a name")
            print("Try again")
