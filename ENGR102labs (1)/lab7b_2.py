#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 7b.2
# Date:		6 March 2019
import math
j = int(input("What is the size of your vector?"))
suma = 0
sumb = 0
dot = 0
vectora= []
vectorb = []
for i in range(j):
    A= int(input("Enter all the next element of the vector A:"))
    vectora.append(A) # adds every number entered to the list containing the vector

for i in range(j):
    B= int(input("Enter all the elements of the vector B:"))
    vectorb.append(B) # adds every number entered to the list containing the vector

sqra = [vectora[i] * vectora[i] for i in range(j)] #squares vector a to be used for magnitude later

sqrb = [vectorb[i] * vectorb[i] for i in range(j)]  #squares vector b to be used for magnitude later

for i in range(j): #this was not the most efficient way of doing this....i'm aware... but it works
    suma += sqra[i] #sums the squared a values
    #the most efficient way would be similar to how I did the dot product (i was short on time)
    magna = math.sqrt(suma) # magnitude of a is the sqrt of the sum
for i in range(j):
    sumb += sqrb[i]
    magnb= math.sqrt(sumb) # magnitude of b


sum = [vectora[i] + vectorb[i] for i in range(j)] # sum of a and b
dif = [vectora[i] - vectorb[i] for i in range(j)] # dif of a and b

for i in range(j):
    mult = vectora[i] * vectorb[i]
    dot += mult #everytime an element of list a is multiplied by an element of list b they sum to the dot product

print("The magnitude of vector a is",magna)
print("The magnitude of vector b is",magnb)
print("The sum of vector a and b is",sum)
print("The difference of vector a and b is", dif)
print("The dot product of vector a and b is,",dot)