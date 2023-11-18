import random
list=['rock','paper','scissors']

user=input("enter your choice, rock paper or scissors: ")

computer=random.choice(list)
print("computer choice:",computer)

#conditions for finalizing who won
if computer=="rock" and user=="paper":
    print("you won!")
elif computer=="rock" and user=="scissors": 
    print("you lost")
elif computer=="rock" and user=="rock":
    print("it is a tie")
elif computer=="paper" and user=="scissors":
    print("you won!")
elif computer=="paper" and user=="rock":
    print("you lost")
elif computer=="paper" and user=="paper":
    print("it is a tie")
elif computer=="scissors" and user=="paper":
    print("you lost")
elif computer=="scissors" and user=="rock":
    print("you won!")
elif computer=="scissors" and user=="scissors":
    print("it is a tie")
