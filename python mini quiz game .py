print("Welcome to my computer quiz game")

playing=input("Do you want to play the game : ?")

if playing.lower() !='yes':
    quit()

print("Okay let's Play the game ")
score=0

answer=input('what does CPU stands for ?')
if answer.lower()=='central processing unit':
    print("correct")
    score +=1
else:
    print("incorrect answer")

answer=input('what does GPU stands for ?')
if answer.lower() ==' Graphic processing unit':
    print("correct")
    score+=1
else:
    print("incorrect answer") 

answer=input('what does RAM stands for ?')
if answer.lower()=='Randam axis memeory':
    print("correct")
    score+=1
else:
    print("incorrect answer")  


answer=input('what does ipl stands for ?')
if answer.lower()=='indian premier league':
    print("correct")
else:
    print("incorrect answer") 


print("you got " + str(score)+"questions correct ")  
print("you got " + str((score / 4) *100)+ '%'.")  







