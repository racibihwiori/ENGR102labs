grades = [87, 93, 75, 100, 82, 91, 85]
sum = 0
for i in range(7): # for things i range 7
# for i in range(len(grades)):
#### sum += grades[i]
##average = sum/len(grades)
#the len operator makes a generic length in the case that you don't know what the length is
    sum += grades[i] #increases sum in each iteration
average = sum/7 # computing average
print(average)