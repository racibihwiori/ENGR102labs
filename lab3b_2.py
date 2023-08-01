#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 3b.2
# Date:		06 FEBRUARY 2019

import math
import numpy as np
from numpy import matrix
xa = float(input('Enter the first observed x value'))
ya = float(input('Enter the first observed y value'))
za = float(input('Enter the first observed z value'))
xb = float(input('Enter the x value of the observer'))
yb = float(input('Enter the y value of the observer'))
zb = float(input('Enter the z value of the observer'))
xc = float(input('Enter the second observed x value'))
yc = float(input('Enter the second observed y value'))
zc = float(input('Enter the second observed z value'))
A = np.array([xa, ya, za])
B = np.array([xb, yb, zb])
C = np.array([xc, yc, zc])
print("Point A is the first observed point, Point B is the observer, Point C is the second observed point.")
print("Together these points create the angle ABC.")
print("Point a is:", A)
print("Point b is:", B)
print("Point c is:", C)

def findvectors(x,y):

    vector = y - x
    return vector

print("The AB Vector is:", findvectors(A, B))
print("The BC Vector is:", findvectors(C, B))

vba = findvectors(A, B)
vbc = findvectors(C, B)

def normalize(a,b,c):
    norm = np.sqrt(a**2+b**2+c**2)
    return norm

normba = normalize(vba[0],vba[1],vba[2])
normbc = normalize(vbc[0], vbc[1], vbc[2])
mbaxbc = normba*normbc #multiplying vector magnitudes for angle function
print("The magnitude of vector BA is",normba,"The magnitude of vector BC is",normbc)

def dotprod(x,y,z,a,b,c):
    dot = x*a+y*b+z*c

    return dot
dotabc = dotprod(vba[0],vba[1],vba[2],vbc[0], vbc[1], vbc[2])

print("The dot product of vector BA and BC is:",dotabc)

def angle(x,y):
    theta = np.arccos((x/y))
    return theta

radabc = angle(dotabc,mbaxbc)

angleabc = np.rad2deg(radabc)

print("Angle ABC is", angleabc, "degrees.")