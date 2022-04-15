import random
from re import L
def compguessit(x):
    feedback=0
    low=1
    high=x
    while feedback != 'c':
        guess=random.randint(low,high)
        print(guess)
        feedback= input(f'''Press "l" if {guess}is too low.\nPress "h" if {guess}is too high.\nPress "c" if {guess}is correct.\n''')
        if feedback=='l':
            low= guess+1
        elif feedback=='h':
            high = guess-1
    print (f"YAY!! {guess} is the right answer.")
compguessit(50)