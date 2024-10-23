import time
name=input("Enter your name")
time.sleep(1)
print("Welcome",name,end="!\n",)
time.sleep(1)
print("You got into gold adventure!! ")
time.sleep(1)
answer=input("you are in the jungile with two ways.which would you like to go(left/right)!:")
time.sleep(1)
if answer.lower()=="right":
    answer=input("You walked a mile and found a bridge with darkness.you would like to go forward or want to head back(forward/cross):")
    time.sleep(1)
    if answer.lower()=="forward":
        print("You found a way with gold filled in a bucket!! ")
    elif answer.lower()=="cross":
        print("You are headed back and died due to lonliness")
    else:
        print("Entered wrong input! Loser!!!")
elif answer.lower()=="left":
    answer=input("You walked a mile and found a bridge with darkness.you would like to go forward or want to head back(forward/cross):")
    time.sleep(1)
    if answer.lower()=="forward":
        print("you attacked by lion and died!")
    elif answer.lower()=="cross":
        print("You are headed back and died due to lonliness")
    else:
        print("Entered wrong input! Loser!!!")
    
else:
     print("Entered wrong input! Loser!!!")
time.sleep(1)
print("That's it.End of the game")