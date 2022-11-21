"""
Name: Task8.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/27/2022
This program will ask the user if they want to convert temperature or speed, then ask the number, the unit, and make the conversion
"""
units = { "1" : { "type" : "weight", "unit" : "kg/lb", "quantity" : 0, "validUnits" : {"kg", "lb"}}, "2" : {"type" : "distance", "unit" : "m/ft", "quantity" : 0, "validUnits" : {"m", "ft"}}}


def conversion(a, b): #First function, for converting temperature
    if a.upper().strip() == "LB": 
        b = 0.451 * b
        c = "kg"
        return b, c
    if a.upper().strip() == "KG":
        b =  b / 0.451
        c = "lb"
        return b, c
    if a.upper().strip() == "M":
        b = b * 3.281
        c = "ft"
        return b, c
    if a.upper().strip() == "FT":
        b = b / 3.281
        c = "m"
        return b, c
            

while True:    #While loop, for repeating the program if the user wants to.
    print("Welcome to Unit conversor!") #Welcome message
    print("")
    print("1. Convert weight") 
    print("2. Convert distance") 
    answer = input("please select one option [1/2]:") #input, for selecting either speed or temperature.
    while not (answer in units.keys()): #while loop, input checker
        answer = input("please select one option [1/2]:")
    while True:
        try:
            units[answer]["quantity"] = float(input("Please type the {} amount (the number can have decimals, and should be greater than 0): ".format(units[answer]["type"])))
        except:
            print("Please type a number.")
        else:
            if units[answer]["quantity"] <= 0:
                continue
            break
    units[answer]["unit"] = str(input("Please type the unit [{}]: ".format(units[answer]["unit"])))
    while not (units[answer]["unit"] in units[answer]["validUnits"]):
        units[answer]["unit"] = str(input("Please type a valid unit: "))
    resultQuantity, resultUnit = conversion(units[answer]["unit"], units[answer]["quantity"])
    print ("{:.2f} {} is equal to {:.2f} {}.".format(units[answer]["quantity"], units[answer]["unit"], resultQuantity, resultUnit))        
    again = input("Do you want to convert again? [y/n]: ") #this input asks the user if they want to repeat the program
    while (again.strip().upper() != "Y") and (again.strip().upper() != "N"):
        again = input("Do you want to convert again? [y/n]: ")
    if again.strip().upper() == "N": #if no, then the program ends
        print("Thanks for using unit conversor. Goodbye!")
        break