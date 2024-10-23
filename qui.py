print("Welcome to quiz Game!")
playing=input("Do you want to play? ")
if playing.lower()!="yes":
    quit()
score=0
print("Okay! Let's play :)")
answer=input("What does cpu stands for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does gpu stands for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does ram stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does psu stands for? ")
if answer.lower()=="power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
print("You got "+str(score)+" answers correct")
print("You got "+str((score/4)*100)+' %')
