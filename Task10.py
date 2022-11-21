# -*- coding: utf-8 -*-
"""
Name: Task10.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/27/2022
This program will find the area and perimeter of a rectangle with a given input of width and height using classes.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculatePerimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    
    def calculateArea(self):
        area = self.width*self.height
        return area

    def displayInfo(self):
        print("\nThe height of the Rectangle is: ", self.height, "centimeters")
        print("The width of the Rectangle is: ", self.width, "centimeters")
        print("The perimeter of the Rectangle is: ", self.calculatePerimeter(), "centimeters")
        print("The area of the Rectangle is: ", self.calculateArea(), "centimeters")
while True:
    try:
        width = int(input("\nPlease enter the width of the Rectangle in centimeters: "))
        height = int(input("\nPlease enter the height of the Rectangle in centimeters: "))
    except:
        print("\nPlease enter a valid number.")
        continue
    else:
        break

result = Rectangle(width, height)

result.displayInfo()