import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

numbers = [1, 2, 3]
player_score = 0
pc_score = 0

while True:

    pc_answer = (random.choice(numbers))

    player_answer = int(input("Choice 1 (rock), 2 (paper), 3 (scissors) : "))

    if pc_answer == 1:
        print("PC answer", rock)
    elif pc_answer == 2:
        print("PC answer", paper)
    elif pc_answer == 3:
        print("PC answer", scissors)
    else:
        print("Try Again")

    if player_answer == 1:
        print("You answer", rock)
    elif player_answer == 2:
        print("You answer", paper)
    elif player_answer == 3:
        print("You answer", scissors)
    else:
        print("Try Again")

    if player_answer == pc_answer:
        print("-->Scoreless ")
    elif player_answer == 1 and pc_answer == 2:
        print("-->PC Win ")
        pc_score += 1
    elif player_answer == 1 and pc_answer == 3:
        print("-->YOU Win ")
        player_score += 1

    if player_answer == 2 and pc_answer == 1:
        print("-->YOU Win ")
        player_score += 1

    elif player_answer == 2 and pc_answer == 3:
        print("-->PC Win ")
        pc_score += 1

    if player_answer == 3 and pc_answer == 1:
        print("-->PC Win ")
        pc_score += 1

    elif player_answer == 3 and pc_answer == 2:
        print("-->YOU Win ")
        player_score += 1

    print(f"PC Score: {pc_score}, Player Score: {player_score}")
    print("--------------------------------------------------------------------------------------------")

    if pc_score == 3:
        print("************* WINNER: PC *************")
        break
    if player_score == 3:
        print("************* WINNER: Player *************")
        break
