# Core Rules
# 🐍 Snake vs. 💧 Water: Snake drinks water; Snake wins.
# 💧 Water vs. 🔫 Gun: Water douses/rusts gun; Water wins.
# 🔫 Gun vs. 🐍 Snake: Gun shoots snake; Gun wins.
# Tie: If both choose the same, it's a Draw.

import random
def computers_choice():
    choices=["s","w","g"]
    return random.choice(choices)

print(""" 
# Core Rules
# 🐍 Snake vs. 💧 Water: Snake drinks water; Snake wins.
# 💧 Water vs. 🔫 Gun: Water douses/rusts gun; Water wins.
# 🔫 Gun vs. 🐍 Snake: Gun shoots snake; Gun wins.
# Tie: If both choose the same, it's a Draw.      
""")

print("🐍 Snake='s' 💧 Water='w' 🔫 Gun='g'")
while (True):
    user_choice=input("enter your choice:")
    if (user_choice=='s' or user_choice=='w' or user_choice=='g'):
        break
    else:
        print("your only allowed choose from above options")
computer_choice=computers_choice()
print("computer'n s choice:",computer_choice)

if(user_choice==computer_choice):
    print("Its a tie!")
else:
    if (user_choice=='s' and computer_choice=='w'):
        print("your win!")
    elif (user_choice=='w' and computer_choice=='g'):
        print("your win!")
    elif (user_choice=='g' and computer_choice=='s'):
        print("your win!")
    else:
        print("computer's win!")