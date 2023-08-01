#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	CFU 3: Cartesian to Polar
# Date:		25 FEBRUARY 2019
import numpy as np
import math
ans = float(input("If you are entering cartesian coordinates enter 1, if you are entering polar coordinates enter 0."))
def getinput():
    x = float(input('What is your x value?'))
    y = float(input('What is your y value?'))
    return (x, y)
(a,b) = getinput()
if ans == 1:
   def cart(x,y):
       r = math.sqrt((x**2) + (y**2))
       p = y/x
       theta = math.atan(p)
       return(r,theta)
   ctop = cart(a, b)
   print('Your polar coordinates are',ctop)

if ans == 0:
    def polar(r,theta):
        x = r*(math.cos(theta))
        y = r*(math.sin(theta))
        return(x,y)
    ptoc = polar(a,b)
    print('Your cartesian coordinates are', ptoc)




