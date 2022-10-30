"""
Name: Task5.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/30/2022
This program will print a dictionary in which the keys are the numbers from 1 to 10 and the values are its cubes.
"""""
cubes = {  #declaring the dictionary
    } 
for i in range (1, 11): #for cycle, 10 times
    cubes[i] = i*i*i #adding new keys to dictionary (i), and assigning the values to be the number's cube (i*i*i)
    
print (cubes) #printing dictionary
 