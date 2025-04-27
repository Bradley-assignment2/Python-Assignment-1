#Creates the function
def average_converting():

    #Calculates the total amount spent during the week
    total_spend = 160 + 75 + 97 + 130 + 100 + 98 + 55

    #Calculates the average spend
    average_spend = total_spend / 7

    #Converts from usd to gbp
    conversion = average_spend * 0.77

    #Returns the converted amount as a string
    return f"Your spending for your trip was £{conversion:.2f}"

#Prints the returned string
print(average_converting())