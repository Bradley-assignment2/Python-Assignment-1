#Imports the re (RegEx) module
import re

#Creates a function
def email_checker():

    #Creates an attempts variable used to count amount of attempts
    attempts = 0

    #Creates a variable used to determine if the loop will continue running
    checking = True

    #Creates a while-loop to allow for up to 3 emails
    while checking is True:

        #Allows the user to enter their email or quit the program
        email = input("Please enter an email address, or type quit to end the program: ")

        #If the user types Quit, stops the loop
        if  email.lower() == "quit":
            checking = False

        #If the user types anything else, the loop continues
        else:

            #Creates a pattern made of letters, symbols and numbers, used to check the validity of an email
            valid_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

            #Uses the RegEx match function to cross-reference the email and the pattern
            #If the email matches the pattern, returns a message
            if re.match(valid_pattern, email):
                print(f"\nEmail is valid\n")

            #If the email doesn't match, returns a different message
            else:
                print(f"\nEmail is not valid\n")

            #Increments the attempts variable by 1
            attempts += 1

            #Ends the loop if user has made 3 attempts
            if attempts == 3:
                checking = False

    #Prints a message when the program has ended
    print(f"Thank you for using my program.")

#Calls the function
email_checker()