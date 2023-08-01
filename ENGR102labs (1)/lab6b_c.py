#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 6b
# Date:		27 FEBRUARY 2019
for i in range(2,101): # iterates from two to one hundred
    for j in range(2, i+1):#checks every value of i as i increments
        if i % j == 0: # if i is divisible by j
            if j<=i: # only if j is less than or equal to i
                print(j,"divides",i)