sum = 0
for i in range(11):
    sum = sum + i
    print(sum)

#while i <= 10:
 #   sum = sum + i
  #  i += 1
#print(sum)
for i in range(3):
    print("i is", i)
    for j in range(3):
        if j > 1: # terminates j is statement after it hits 1
            break # Forces termination of a block
        print(" j is", j)
