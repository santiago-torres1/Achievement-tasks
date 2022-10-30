"""
Name: Task6.py
Author: Santiago Torres
Date created: 10/24/2022
Date last modified: 10/30/2022
This program will ask the user for a group of numbers, and will display two groups: one for prime numbers and one for non prime numbers
"""
def isPrime(n): #function for checking if a number is prime or not
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

nonPrimes = [] #first list, non primes
primes = [] #second list, primes
numbers = list(map(str, input("Please enter the numbers: ").split(","))) #input from the user, it divides the number using "," separator
for i in range (0, len(numbers)): #for loop, will repeat the process depending on how many numbers the user typed
    number = int(numbers[i])
    if isPrime(number) == False:
        nonPrimes.append(numbers[i]) #this condition will add the nonprime numbers to nonprime list
    else:
        primes.append(numbers[i]) #this condition will add the prime numbers to the primes list

print("prime numbers are: ", ", ".join(primes)) #first display, it will print the prime number list
print("Non Prime numbers are: ", ", ".join(nonPrimes)) #second display, it will print the nonprime number list