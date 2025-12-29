import random

is_running=True
guess = random.randint(1,10)
count = 0

while is_running:
    user_number = int(input("enter a number between 1 and 10: "))
    if user_number < guess :
        print("the guess number is higher, try again: ")
        count += 1
    elif user_number > guess :
        print("the guess number is lower, try again: ")
        count += 1
    else :
        count += 1
        print("congratulations, you have found it")
        print(f"you found it after {count} tries")
        is_running = False
