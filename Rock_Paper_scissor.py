import random
user_wins=0
computer_wins=0
options=["rock","paper","scissor"]
while True:
    user_input=input("Type Rock Paper Scissor or q:")
    if user_input=='q':
        break
    if user_input not in options:
        print("Enter Again")
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer picked",computer_pick+".")
    if computer_pick==user_input:
        print("Draw")
    elif user_input=="paper" and computer_pick=="rock":
        print("You Won")
        user_wins+=1
     
    elif user_input=="rock" and computer_pick=="scissor":
        print("You Won")
        user_wins+=1
    elif user_input=="scissor" and computer_pick=="paper":
        print("You Won")
        user_wins+=1   
    else:
        print('You lose')
        computer_wins+=1
        
print("computer",computer_wins,"\nyou",user_wins)   
    