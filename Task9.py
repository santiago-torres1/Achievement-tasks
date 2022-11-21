""""
Name: Task9.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/30/2022
This program will ask the user to register courses, and then display the user's information.
"""
import os
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
for i, j in courses.items(): #printing the dictionary with the courses
    print(i,"-", j)
courseRegistration = list(map(str, input("Please type the courses you want to register (use this format: AAAA0000, AAAA1111, AAAA2222, etc): ").split(", "))) #getting the courses from user
for i in range (0, len(courseRegistration)):
    while courseRegistration[i] not in courses.keys(): #input checker
        print("")
        print("Sorry, you entered a wrong course code. Please try again.")
        courseRegistration = list(map(str, input("Please type the courses you want to register (use this format: AAAA0000, AAAA1111, AAAA2222, etc): ").split(", ")))
aFile = open("D:\College\Programming\Codes\info.txt", "w")
aFile.write("Student name: \t {} {}".format(student["firstName"], student["lastName"]).expandtabs(50))
aFile.write("\nStudent number: \t {}".format(student["studentNumber"]).expandtabs(50))
aFile.write("\nTotal number of registered courses: \t {}".format(len(courseRegistration)).expandtabs(50))
aFile.write("\n{0:-^80s}".format(''))
a=1
for i in courseRegistration:
    aFile.write("\nCourse #{}: {} - {}".format(a, courses.get(i), i))
    a=a+1
print("Your data has been succesfully saved in: ", os.path.dirname(r"D:\College\Programming\Codes\info.txt"))
aFile.close()
