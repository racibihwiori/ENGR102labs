#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 5b
# Date:		20 FEBRUARY 2019
import numpy as np
#Create o,a,b,c,d arrays using 4 x values and 4 y values
#all estimated from the stress strain graph of steel.
O = np.array([0, 0])
AB = np.array([.01, 42])
C = np.array([.052, 43])
D = np.array([.175, 60])
E = np.array([.26, 43])
#Define the slope of four line segments:
#young modulus, plastic, strain hardening, and max strength
#do this by 2D interpolating points O, AB, C, D, E as needed.

def youngm(ax,ay,bx,by):
    m = by-ay/bx-ax
    return(m)

def plastic(bx,by,cx,cy):
    m = cy-by / cx-bx
    return(m)
def strain(cx,cy,dx,dy):
    m = dy-cy / dx-cx
    return(m)
def maxs(dx,dy,ex,ey):
    m = ey-dy / ex-dx
    return(m)
def printeq(a,b,c,d):
    print("Young modulus aka modulus of elasticity is the slope of a stress strain in the linear elastic region.")
    print("The young modulus equation of the steel stress strain curve is:",a,"*x")
    print("The plastic equation of the steel stress strain curve is:",b,"*x")
    print("The strain hardening equation of the steel stress strain curve is:",c,"*x")
    print("The max strength equation of the steel stress strain curve is:",d,"*x")
ymeq = youngm(O[0], O[1],AB[0], AB[1])
pleq = (plastic(AB[0],AB[1],C[0],C[1]))*-1
sthd = (strain(C[0],C[1],D[0],D[1]))*-1
mxst = (maxs(D[0],D[1],E[0],E[1]))*-1
printeq(ymeq, pleq, sthd, mxst)

#Read in user input for stress, specify in ksi
stress = float(input('Enter the Stress of the standard steel in ksi:'))
# stress(y) = m(the young modulus lin approximation) * x (the strain)
if stress < 0:
    strain = (stress*-1) /ymeq #rearrange the equation to find strain
    #catches the edge case in which user inputs negative number
else:
    strain = stress/ymeq #rearrange the equation to find strain

print("Your strain value is:",strain,"based on the linear elastic slope of the steel stress curve.")
#Print the strain value, clarifying it is based on the linear elastic approximation.
