#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 3b.1a
# Date:		06 FEBRUARY 2019
m = float(input('Enter object mass:'))
v = float(input('Enter object velocity:'))
def findke(x,y):
    kine = (x*y**2)/2
    return kine
kin = findke(m,v)
print('The kinetic energy of this object is',kin)