

def Jono(input_integer):
    twoUp = input_integer + 2
    twoDown = input_integer - 2
    return (twoUp,twoDown) #return tuple
print(Jono(3))

def Sum(X) :
    Y = 5 + X
    return Y
xx = int(input())
print(Sum(5))
print(Sum(xx))

f = float(input("Enter your temperature:"))
if f < 32:
    print('Water is in solid phase')
elif (f>32) and (f<212):
    print('Water is in liquid phase')
elif f>212:
    print('Water is in gaseous phase')
elif f == 32:
    print('Water is either liquid or gaseous')
p = 3
if p>6:
    print('Yes')
elif p<6:
    print("no")