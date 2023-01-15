print("Welcome to the quiz game :) ")

lets_play = input("Do you wanna play ? ")
print(lets_play)

if lets_play.lower() == "yes" :
    print("OK! let's play :) ")
else :
    quit()                               #it is a function
score = 0 

answer = input("what does CPU stand for ? ")
if answer.lower() == "central processing unit" :
    print("correct! :) ")
    score += 1
else :
    print("incorrect! :( ")

answer = input("what does gpu stand for ? ")
if answer.lower() == "graphics processing unit" :
    print("correct! :) ")
    score += 1
else :
    print("incorrect! :( ")

answer = input("what does RAM stand for ? ")
if answer.lower() == "random access memory" :
    print("correct! :) ")
    score += 1
else :
    print("incorrect! :( ")

answer = input("what does PSU stand for ? ")
if answer.lower() == "power supply unit" :
    print("correct! :) ")
    score += 1
else :
    print("incorrect! :( ")

print("your total score is : " , str(score) )
print("your total score percentage is : " ,  str((score/4) * 100) , "%")

