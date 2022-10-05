"""
Name: Task1.py
Author: Santiago Torres
Date created: 10/03/2022
Date last modified: 10/05/2022
This program will calculate area and perimeter of a circle, a rectangle or a triangle.
"""

print ("Geometry Calculator") #We start our program with a welcome message
print (" ") #This includes a space in between
while True: #This While loop is made for repeating the program until the user wants to quit
    print ("1. Calculate the area of circle" + "\n" + "2. Calculate the area of a rectangle" \
       + "\n" + "3. Calculate the area of a triangle" + "\n" + "4. Quit") #This are the options displayed for the user
    answer = input ("Please select an option (1-4): ") #This is the variable that stores the user's input

    if (answer == "1"): #First condition, if the user types "1"
        radius=float(input("Please enter the radius of your circle in centimeters: ")) #As user selected the circle, the program asks for the radius
        areaCircle = 3.1416*radius*radius #This line calculates the area with the formula pi multiplied by squared radius and stores the value in areaCircle variable
        perimeterCircle = 2*3.1416*radius #This line calculates the perimeter (circunference) of the circle using the formula two times pi multiplied by radius and stores the value in perimeterCircle variable 
        print ("The area of your circle is: ", areaCircle , "cm2") #This displays the result of the area in cm2
        print ("The perimiter of your circle is: ", perimeterCircle , "cm") #This displays the result of the perimeter in cm
        questionContinue =  input("Do you wish to calculate another area?[yes/no]") #This line asks the user if they want to calculate another area
        if questionContinue.strip().upper() == "NO": #this is the condition if they say no. It does not matter if the user types in upper case or lower case, or if the user types a space, the program won't have an error.
            print (" ") #This is a blank space so the program looks organized
            print ("Thank you for using Geometry Calculator!") #This is a goodbye message.
            break #this breaks the loop and ends the program.
        elif questionContinue.strip().upper() == "YES": #this is the condition if they say yes. It does not matter if the user types in upper case or lower case, or if the user types a space, the program won't have an error.
            continue #this restarts the while loop
            
    elif (answer == "2"): #Second condition, if the user types "2"
        baseRectangle=float(input("Please enter the lenght of the base of your rectangle in centimeters: ")) #As user selected rectangle, the program first asks for the base of the rectangle
        heightRectangle=float(input("Please enter the height of your rectangle in centimeters: ")) #Then, the program asks for the height
        areaRectangle = baseRectangle*heightRectangle #Calculating the area of the rectangle
        perimeterRectangle = 2*(baseRectangle+heightRectangle) #Calculating the perimeter of the rectangle
        print ("The area of your rectangle is: ", areaRectangle , "cm2") #Displaying rectangle area
        print ("The perimiter of your rectangle is: ", perimeterRectangle , "cm")#Displaying rectangle perimeter
        questionContinue =  input("Do you wish to calculate another area?[yes/no]") #As the previous one, this if condition asks the user if they want to continue calculating; the next lines are the same.
        if questionContinue.strip().upper() == "NO":
            print (" ")
            print ("Thank you for using Geometry Calculator!")
            break
        elif questionContinue.strip().upper() == "YES":
            continue     
        
    elif (answer == "3"): #Third condition, if the user types "3"
        baseTriangle=float(input("Please enter the lenght of the base of your triangle in centimeters: ")) #In this case, for calculating the area and perimeter of a triangle, we need to know the length of the 3 sides and the height. First, we ask for the base.
        side2Triangle=float(input("Please enter the lenght of the second side of your triangle in centimeters: ")) #Now we ask for the length of second side
        side3Triangle=float(input("Please enter the lenght of the third side of your triangle in centimeters: ")) #Then we ask for the length of third side
        heightTriangle=float(input("Please enter the height of your triangle in centimeters: ")) #And finally we ask for the height
        areaTriangle = baseTriangle*heightTriangle/2 #Calculating area of triangle
        perimeterTriangle = baseTriangle + side2Triangle + side3Triangle #Calculating perimeter of triangle
        print ("The area of your triangle is: ", areaTriangle , "cm2") #Displaying area of triangle
        print ("The perimiter of your triangle is: ", perimeterTriangle , "cm") #Displaying perimeter of triangle
        print (" ") #A space in between for a better organized look.
        questionContinue =  input("Do you wish to calculate another area?[yes/no]") #One more time, we ask the user if he wants to continue.
        if questionContinue.strip().upper() == "NO":
            print (" ")
            print ("Thank you for using Geometry Calculator!")
            break
        elif questionContinue.strip().upper() == "YES":
            continue
        
    elif (answer == "4"): #Fourth condition, if the user typer "4"
        print (" ")
        print ("Thank you for using Geometry Calculator!") #Goodbye message
        break  #As the user selected the option 4: Quit, we end the loop and finalize the program.
    
    else: #Last condition, just in case the user types anything different from 1, 2, 3 or 4.
        print (" ") 
        print ("Please enter a valid option") #Message
        print (" ")