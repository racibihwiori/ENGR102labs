#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	CFU 4: Fizz buzz
# Date:		27 FEBRUARY 2019
a = int(input("Enter a first positive number"))
b = int(input("Enter a second positive number"))
c = int(input("Enter the limit for the game"))
for i in range(1,c):
    if i%a==0:
        if i%b==0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    if i%a!=0 and i%b==0:
        print("Buzz")
    if i%a!=0 and i%b!=0:
        print(i)