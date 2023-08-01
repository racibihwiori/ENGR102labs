#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 6b
# Date:		27 FEBRUARY 2019
a = float(input("Enter a positive number"))
i = 0
def collatz(n):
        if n % 2==0:
            n = (n/2)
            print(n)
            return (n)

        elif n % 2==1:
            n = (3*n+1)
            print(n)
            return (n)
while a != 1:
    i += 1
    a = collatz(a)

print("There were",i,"iterations to reach 1.")
