#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	CFU 1
# Date:		11 FEBRUARY 2019
x = (input('What is your name?'))
a = float(input('How many As did you make?'))
b = float(input('How many Bs did you make?'))
c = float(input('How many Cs did you make?'))
d = float(input('How many Ds did you make?'))
y = int(a+b+c+d)

gpa = (a*4 + b*3 + c*2 + d*1)/(y)

print('Howdy',x,'! Based on your grades from',y,'classes, your GPA is:',gpa)