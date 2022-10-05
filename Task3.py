"""
Name: Task1.py
Author: Santiago Torres
Date created: 10/03/2022
Date last modified: 10/05/2022
This program will ask the user for an username, and if it does not meet the conditions, it will ask for another until conditions are fullfilled.
"""
global i #First, we declare a global variable that we will use later.
i=0 #We assign value 0 to the variable

def checkForUpperAndNumbers (checkUpperNumbers): #This funcion checks if the username typed by the user has 1 upper case letter AND 1 number
    if checkUpperNumbers.strip().islower() or checkUpperNumbers.strip().isalpha():    #This condition checks if all the characters are lower case OR all characters are letters (no numbers). If either one of those is true, the program will show an error message.   
        print ("Sorry, username should include at least one upper case letter and one number")    #error message
    elif checkUpperNumbers.isnumeric(): #This condition checks if all the characters are numbers, and if so, displays an error message
        print ("Sorry, username should include at least one upper case letter and one number")    #error message
    else: #If the program reaches this last condition, it means that the username meets all the requirements for this function (1 upper case and 1 number)
        global i #We call the variable again
        i = i+1 #We add 1 to the variable, this will be explained in detail in the While loop
        return i #We return the value of i
        return (checkUpperNumbers) #We return the value of the username.
    
def checkForLength (checkLength): #This function checks if the username meets the length requirements (between 2-20 characters).
    if len(checkLength) == 1: #This conditional check if the username has just 1 character
        print("Sorry, username must be longer than 1 character.") #Displays error message
        return (checkLength) #Returns value to the loop
    elif len(checkLength) > 20: #This conditional checks if the username has more than 20 characters.
        print("Sorry, username cannot contain more than 20 characters.") #Displays error message
        return (checkLength) #Returns value to the loop
    else: #If the program reaches this point, it means that username length is between 2 and 20, which is good.
        global i #We call the variable again
        i = i+1 #We add 1 to the variable, this will be explained in detail in the While loop
        return i #We return the value of i
        return (checkLength) #We return the value of the length of the username.


while i<=2: #Finally, the loop. This loop will repeat as long as variable i is equal or lower than 2. Why 2? Because there are two functions that check username requirements, and when the requirements
            #are met, each function adds 1 to the value of i. So, when both functions add 1, that means, when all the requirements are met, the loop will stop (See if condition below)
    i=0 #This resets i value. This is done because, for example, in the first time, user types an username that meets 1 of 2 requirements, then the function would add 1 to the value of the variable,
        #and that value will be stored, so the next time the user types an username, even if they only meet 1 of 2 requirements again, the program will stop because the value of 2 will be reached,
        #so, to avoid that, we reset the value of i back to 0.
    username = input("Please type your username: ") #this line asks the username to the user
    checkForUpperAndNumbers(username) #this line executes the function that checks if the username has uppercase and numbers
    checkForLength(username) #this line executes the funcion that checks if the username length is between 2 and 20.
    if len(username)==0: #this condition resets the loop just in case the user presses enter without typing anything before.
        continue #this continues the loop
    if i==2: #When the value of variable i reaches 2 (when all conditions are met) this condition will display a message and end the program
        print("Username" , username.strip() , "accepted!") #message displaying that the username was accepted
        break #end of the program