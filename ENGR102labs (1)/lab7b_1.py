#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name: 		Rachel Ibihwiori
# Section:		ENGR 102-512
# Assignment:	Lab 7b.1
# Date:		6 March 2019
i = 0 #using i to create a loop
stop = "stop" # stop variable is a list of letters in stop
while i == 0: #using a while loop that can only be broken by the word stop
    word = (input('Enter one word:'))
    if word == stop:
        break #loop breaks when the word the user enters is equal to the stop variable(the word stop)

    if word[0] in "aeiouy": #if the first letter of the word(first index of list) includes any of aieou (vowels)
        print(word+"yay") # adds yay to the original word

    else: #if the word does not begin with a vowel
        firlet = word[0] + "ay" #creates the end part of pig latin which is the first letter plus ay
        pigl = word[1:] + firlet #takes all the letters in the word after the first letter (index 0) and adds the end part
        print(pigl)
