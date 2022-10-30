""""
Name: Task4.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/30/2022
This program will ask the user to register courses, and then display the user's information.
"""
student = { #first dictionary, for student information
    "firstName" : "",
    "lastName" : "",
    "studentNumber" : "",
    }

courses = { #second dictionary, for the available courses
    "INFO1250" : "Computer Systems Fundamentals",
    "CDEV1830" : "Career Success",
    "PROG1783" : "Programming Fundamentals",
    "INFO1385" : "Network Infrastructure"
    }

student["firstName"] = (input("Please enter your first name: ")) #inputs for student information
student["lastName"] = (input("Please enter your last name: "))
student["studentNumber"] = (input("Please enter your student number: "))

print("")
print("These are the courses available for you: ")
for key, value in courses.items(): #printing the dictionary with the courses
    print(key, value)
courseRegistration = list(map(str, input("Please type the courses you want to register (use this format: AAAA0000, AAAA1111, AAAA2222, etc): ").split(", "))) #getting the courses from user
for i in range (0, len(courseRegistration)):
    while courseRegistration[i] not in courses.keys(): #input checker
        print("")
        print("Sorry, you entered a wrong course code. Please try again.")
        courseRegistration = list(map(str, input("Please type the courses you want to register (use this format: AAAA0000, AAAA1111, AAAA2222, etc): ").split(", ")))
print("")            
print("Full name:", student["firstName"], student["lastName"]) #lastly, the print functions that display all the information.
print("Student number:", student["studentNumber"])
print("Registered courses: ")
for i in courseRegistration:
    print(courses.get(i), "(code: " + i + ")")