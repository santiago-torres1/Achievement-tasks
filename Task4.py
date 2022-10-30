"""
Name: Task4.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/27/2022
This program will ask the user if they want to convert temperature or speed, then ask the number, the unit, and make the conversion
"""
        
def conversionTemperature(a, b): #First function, for converting temperature
    if a.upper().strip() == "F": 
        b = 5/9 * (b - 32)
        return b
    elif a.upper().strip() == "C":
        b = 9/5 * b + 32
        return b
            
def conversionSpeed(a, b): #Second function, for converting temperature
    if a.upper().strip() == "MPH":
        b = 1.609 * b
        return b
    elif a.upper().strip() == "KMH":
        b = b / 1.609
        return b

def otherUnit(a): #Third function, will be used in the display of the result. This function will just print the other unit that was not used.
    if a.strip().upper() == "F":
        return "C"
    elif a.strip().upper() == "C":
        return "F"
    elif a.strip().upper() == "MPH":
        return "KMH"
    elif a.strip().upper() == "KMH":
        return "MPH"
         
while True:    #While loop, for repeating the program if the user wants to.
    print("Welcome to Unit conversor!") #Welcome message
    print("")
    print("1. Convert temperature") 
    print("2. Convert speed") 
    magnitude = input("please select one option [1/2]:") #input, for selecting either speed or temperature.
    while not((magnitude.strip() == "1") or (magnitude.strip() == "2")): #while loop, input checker
        magnitude = input("please select one option [1/2]:")
    if magnitude.strip() == '1': #if user selects temperature, the program then asks for the quantity and the unit.
        temperatureNumber = int(input("Please enter the temperature number: "))
        temperatureUnit = str(input("Please enter the temperature unit [C/F]:"))
        while (temperatureUnit.strip().upper() != "C") and (temperatureUnit.strip().upper() !="F"): #input checker
            temperatureUnit = str(input("Please enter the temperature unit [C/F]:"))
        print("{} °{} is equivalent to: {:.1f} °{}".format(temperatureNumber, temperatureUnit, 
                conversionTemperature(temperatureUnit, temperatureNumber), otherUnit(temperatureUnit))) #this print displays the result
    elif magnitude.strip() == '2': #if user selects speed, the program then asks for the quantity and the unit.
        speedNumber = int(input("Please enter the speed number: "))
        speedUnit = str(input("Please enter the speed unit [KMH/MPH]:"))
        while (speedUnit.strip().upper() != "KMH") and (speedUnit.strip().upper() != "MPH"): #input checker
            speedUnit = str(input("Please enter the speed unit [KMH/MPH]:"))
        print("{} {} is equivalent to: {:.1f} {}".format(speedNumber, speedUnit, 
                conversionSpeed(speedUnit, speedNumber), otherUnit(speedUnit)))     #this displays the result
    again = input("Do you want to convert again? [y/n]: ") #this input asks the user if they want to repeat the program
    while (again.strip().upper() != "Y") and (again.strip().upper() != "N"):
        again = input("Do you want to convert again? [y/n]: ")
    if again.strip().upper() == "N": #if no, then the program ends
        break
    elif again.strip().upper() == "Y":
        continue