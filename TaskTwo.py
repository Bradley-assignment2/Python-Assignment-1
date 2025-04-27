#Creates the function
def cash_machine():

    #Sets the balance to the amount in the task description
    balance = 231


    #Sets the withdrawal limit to the amount in the task description
    maximum_withdraw = 250

    #Sets the minimum withdrawal amount to 10
    #This prevents users from using values below 0
    minimum_withdraw = 10

    #Prints the current balance
    print(f"Your balance is £{balance}")

    #Sets the amount of attempts to 0
    attempts = 0

    #Repeats the loop up to 3 times if an incorrect value is inputted,
    #If a correct value is selected before this the loop will end
    while attempts < 3:

        #Asks for the withdrawal amount
        withdraw = input(f"\nHow much would you like to withdraw: £")


        try:
            #Tries to convert the Withdraw variable to int,
            #if it is not possible (if the user inputs letters/symbols or a float)
            #It will return an error message, and the loop will restart
            withdraw = int(withdraw)

            #Checks if the withdrawal amount is below the minimum withdrawal amount,
            #prints a message to inform the user
            if withdraw < minimum_withdraw:
                print(f"\nSorry, the minimum withdrawal amount is £10. Please try again.")

            #Checks if the withdrawal amount is above the maximum withdrawal amount,
            #prints a message to inform the user
            elif withdraw > maximum_withdraw:
                print(f"\nSorry, the maximum withdrawal amount is £250. Please try again.")

            #Checks if the withdrawal amount is more than the balance,
            #prints a message to inform the user
            elif withdraw > balance:
                print(f"\nSorry, you do not have enough to withdraw that amount. Please try again.")

            #Checks if the withdrawal amount is not divisible by 10,
            #This is used to limit withdrawal to £10 and £20 notes.
            #Prints a message to inform the user
            elif withdraw % 10 != 0:
                print(f"\nSorry, withdrawals can only be made up of £10 and £20 notes. Please try again.")

            #If no errors occur, takes the withdrawal amount away from the balance,
            #prints a message with the final balance.
            else:
                final_balance = balance - withdraw
                print(f"\nWithdrawal successful, your balance is now £{final_balance}.")

                #Adds 4 to the attempts variable to end the loop,
                #this also skips an error message designed to show up if too many incorrect attempts are made
                attempts += 4

        #Prints an error message if the user inputs a string/any incorrect datatype
        except ValueError:
             print(f"\nError, please enter a number.")

        #Adds 1 to the "attempts" variable
        attempts += 1

    #Returns an error message if too many incorrect attempts have been made
    if attempts == 3:
        return f"\nYou have made too many incorrect attempts. Please contact your bank."

    #Returns a "thank you" message if the withdrawal was successful
    else:
        return f"\nHave a nice day!"

#Calls the function inside a print statement
print(cash_machine())