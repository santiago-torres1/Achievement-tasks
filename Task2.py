"""
Name: Task2.py
Author: Santiago Torres
Date created: 10/03/2022
Date last modified: 10/05/2022
This program will calculate area and perimeter of a circle, a rectangle or a square using functions.
"""

"""
Pseudocode:
    Define functions used in the program
    Display welcome message
    Display menu showing options
    Ask the user to select geometric shape
    According to the user's selection, ask for dimensions in cm
    Trim any spaces that user could typed in the input
    Calculate area and perimeter
    Display results in cm2 (area) and cm (perimeter)
    Ask the user if they want to calculate another area
    If so, restart; if not, end the program.
"""

global i # We start our program by defining a global variable which we will use further in the program
i=1 #We assign value 1 to the variable. 

def square(side): #We define the function for the square.
    areaSquare = side * side #This line calculates the area of the square
    perimeterSquare = 4 * side #This line calculates the perimeter of the square
    print ("The area of your square is ", areaSquare, "cm2")  #This displays the area of the square
    print ("The perimeter of your square is ", perimeterSquare, "cm") #This displays the perimeter of the square
    
def rectangle(base, height): #We define the function for the rectangle
    areaRectangle = base * height #This line calculates the area of the rectangle
    perimeterRectangle = 2 * (base + height) #This line calculates the perimeter of the rectangle
    print ("The area of your rectangle is ", areaRectangle, "cm2") #This displays the area of the rectangle
    print ("The perimeter of your rectangle is ", perimeterRectangle, "cm") #This displays the perimeter of the rectangle
    
def circle(radius): #We define the function for the circle. It is the same as before: Two calculations and two displays, one for the area and one for the perimeter.
    areaCircle =  3.1416 * radius * radius
    perimeterCircle = 2 * 3.1416 * radius
    print ("The area of your circle is ", areaCircle, "cm2")
    print ("The perimeter of your circle is ", perimeterCircle, "cm")
    
def continueProgram(answer): #We define the function for repeating the program is the user wants to calculate another area, and for ending the program if the user wants to quit
    if questionContinue.strip().upper() == "NO": #this is the condition if they say no. It does not matter if the user types in upper case or lower case, or if the user types a space, the program won't have an error.
        print (" ") #This is a blank space so the program looks organized
        print ("Thank you for using Geometry Calculator!") #This is a goodbye message.
        global i #This calls the i variable we declared at the beginning.
        i = i+1 #This adds 1 to the value of i variable. This is done for ending the While loop.
        return i #This returns the value of i to the loop for ending it.
    elif questionContinue.strip().upper() == "YES": #this is the condition if they say yes. It does not matter if the user types in upper case or lower case, or if the user types a space, the program won't have an error.
        return True #this restarts the while loop
    
print ("Geometry Calculator") #This is a header message
print (" ") #This includes a space in between
    
while i==1: #This While loop is made for repeating the program until the value of i changes. It will change only when the user wants to quit.
    print ("1. Calculate the area of a square" + "\n" + "2. Calculate the area of a rectangle" \
       + "\n" + "3. Calculate the area of a circle" + "\n" + "4. Quit") #This are the options displayed for the user
    answer = input("Please select an option (1-4): ") #This is the variable that stores the user's input

    if (answer.strip() == "1"): #First condition, if the user types "1"
        sideLength = float(input("Please type the lenght of the side of the square in cm: ")) #This line asks the length of the square, as option 1 is square
        square(sideLength) #this line uses the square function defined previously.
        questionContinue =  input("Do you wish to calculate another area?[yes/no]") #This line asks the user if they want to calculate another area
        continueProgram(questionContinue) #this line uses the continueProgram function for continuing or ending the program.
        
    elif (answer.strip()  == "2"): #Second condition, if the user types "2"
        baseRectangle=float(input("Please enter the lenght of the base of your rectangle in centimeters: ")) #As user selected rectangle, we need to ask them the length and height of the rectangle.
        heightRectangle=float(input("Please enter the height of your rectangle in centimeters: "))
        rectangle(baseRectangle, heightRectangle) #this line uses the rectangle function defined previously.
        questionContinue =  input("Do you wish to calculate another area?[yes/no]")
        continueProgram(questionContinue) #this line uses the continueProgram function for continuing or ending the program.
        
    elif (answer.strip()  == "3"): #Third condition, if the user types "3"
        radius = float(input("Please type the radius of the circle in cm: ")) #In this case we need the radius as option 3 is circle
        circle(radius) #this line uses the circle function defined previously.
        questionContinue =  input("Do you wish to calculate another area?[yes/no]") #This line asks the user if they want to calculate another area
        continueProgram(questionContinue) #this line uses the continueProgram function for continuing or ending the program.
        
    elif (answer.strip()  == "4"): #Fourth condition, if the user decides to quit
        print (" ")
        print ("Thank you for using Geometry Calculator!") #Goodbye message
        break  #break that ends the program
    
    else: #This is done just in case the user types something different from 1, 2, 3 or 4.
        print (" ")
        print ("Please enter a valid option") #message
        print (" ")