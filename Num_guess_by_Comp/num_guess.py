#Letting the computer guess your Number

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # it can be low or high since low == high.
        print("Please enter (h) If the number guessed by the computer is Higher than your number, (l) If it's Lower and (c) If it's the Correct number.\n")
        feedback = input(f"Is {guess}, High(h), Low(l), or Correct(c)??\n")
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
            
    print(f"Yeahh! Finally the computer guessed your number, {guess}, correctly!")

computer_guess(1000)  #You can update the value, it's upto you :)