import random

print("Let's guess the random number. It is generated between min and max that you decide.")

min = ""
while(not min.isdecimal()):
    min = input("Please input the minimum number: ")
    if(not min.isdecimal()):
        print("Sorry, your input is not decimal.")

max = ""
while(not max.isdecimal() or int(min) >= int(max)):
    max = input("Please input the maximum number: ")
    if(not max.isdecimal()):
        print("Sorry, your input is not decimal.")
    elif(int(min) >= int(max)):
        print("Sorry, maximum number should be larger than the minimum number.")

min = int(min)
max = int(max)

ans = random.randint(min, max)
guess = ""
while(not guess.isdecimal() or ans!=int(guess)):
    guess = input("Please input your guess: ")
    if(not guess.isdecimal()):
        print("Sorry, your input is not decimal.")
    elif(ans != int(guess)):
        print("Your guess is wrong. The answer is not " + guess + ".")

print(f"Conguratulation! The answer is {ans}.")