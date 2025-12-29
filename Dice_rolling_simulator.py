#simulate rolling a die. Add cool features like rolling multiple dice or cou ting the frequency

import random

number_of_dice= int(input("enter your number of dice: "))
for i in range(1,number_of_dice+1   ):
    print(f"dice number {i}: ")
    turn = random.randint(1, 6)
    print(turn)
#print(turn)