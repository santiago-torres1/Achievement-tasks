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
        print("Sorry, username must be longer than 1 character.")
        return (checkLength)
    elif len(checkLength) > 20:
        print("Sorry, username cannot contain more than 20 characters.")
        return (checkLength)
    else:
        global i
        i = i+1
        return i
        return (checkLength)


while i<=2:
    i=0
    username = input("Please type your username: ")
    checkForUpperAndNumbers(username)
    checkForLength(username)
    if len(username)==0:
        continue
    if i==2:
        print("Username" , username.strip() , "accepted!")
        break