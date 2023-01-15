import random

highest_range = input("please enter any number ")

if highest_range.isdigit() :
    highest_range = int(highest_range)

    if highest_range < 0 :
        print("please enter a number greater than 0 next time ")
        quit()
else :
    print("please enter a number next time ")
    quit()

random_number = random.randrange(1 , highest_range)             #we can also randint instead of randrange


guesses = 0

while True :
    guesses += 1 
    user_guess = input("Make a guess ")
    if user_guess.isdigit() :
        user_guess = int(user_guess)
    else :
        print("please type a number next time")
        continue 
    
    if user_guess == random_number :
        print("you got it !!!")
        break
    elif user_guess > random_number :
        print("your guess is above the number ")
    else :
        print("your guess is below the number ")
        
print("you got correct guess in " , guesses , "guesses")
