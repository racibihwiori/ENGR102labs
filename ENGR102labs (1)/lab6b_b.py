#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 6b
# Date:		27 FEBRUARY 2019
i = 0
j=0
sum=0
newmax = 0
newmin= 0
while i >= 0:
    i = float(input("Enter your measurements, when you've finished, enter negative one."))
    if i>=0:
        j+=1 #counting how many values have been entered
        sum+=i #create a sum of all values entered
        if i >newmax: #if first number is greater than 0 it is the new max,
            # then each number added from the user is then checked if its greater than the last
            newmax= i

        if i <newmax:
             i = newmin

    if i<0:
       break #stops loops when i is negative

def ave(x,y): #
    avg =x/y
    return(avg)
mean = ave(sum,j)
print("For the given set of number the mean is:",mean)
print("The max value is:",newmax)
print("The min value is",newmin)