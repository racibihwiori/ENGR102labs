print("See if you can guess the number I'm thinking of!")
secret_number = 7
user_guess = int(input("Guess a number from 1 to 10:")) #guess first outside of while loop
numguess = 1 #times you tried to guess starts at 1
while user_guess != secret_number:
    print("No! Try again.")
    numguess +=1 #serves as a counter
    user_guess = int(input("Guess a number from 1 to 10: ")) #guess again inside the while loop
print("You guessed it! It took you",numguess,"tries.")

#a = 0
#while a == 0:
   # print("About to change a")
  #  a =1
   # print("Changing back to 0")
 #   a = 0
i = 0 #initialize
while i < 10: #condition :: i<= 10 is better than i < 11
    print("doing something")
    i += 1 # increment
# or
i = 1
while i <= 10:
    print("doing something...")
    i += 1
    #this loop will stop when i = 10
# for loop is when you know exactly how many times you want to do something
for i in range(10): #range function creates list of numbers from 0 to 9
    print(i) # for each item in this list do this