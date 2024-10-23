import random
top_of_num=input("Enter top of range:")
if top_of_num.isdigit():
    top_of_num=int(top_of_num)
    if top_of_num<=0:
        print("Enter number greater than zero next time")
        quit()
else:
    print("Enter number next time")
    quit()
rand=random.randint(0,top_of_num)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a Guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please Enter a number next time")
        continue
    if user_guess==rand:
        print("You got it")
        break
    elif user_guess>rand:
            print('You are above the number')
    else:
            print("You are below the number")
print("You got in",guesses,"guesses")