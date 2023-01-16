import random

user_wins = 0                       
ai_wins = 0

options = ["rock" , "paper" , "scissors"]

while True :
    user_input = input("enter rock/paper/scissors or Q to quit : ").lower()
    if user_input == "q" :
        break

    if user_input not in options :
        continue 

    random_number = random.randint(0 , 2)
    #rock 0 , paper 1 , scissors 2 
    ai_pick = options[random_number]
    print("ai_picked " , ai_pick )

    if user_input == "rock" and ai_pick == "scissors" :
        print("you won!!")
        user_wins += 1

    elif user_input == "paper" and ai_pick == "rock" :
        print("you won!!")
        user_wins += 1 

    elif user_input == "scissor" and ai_pick == "paper" :
        print("you won!!")
        user_wins += 1

    else :
        print("ai_wins")
        ai_wins += 1
print("GoodBye!!!")    
