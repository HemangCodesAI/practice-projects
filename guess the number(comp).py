import random
def guessit(x):
    cans = random.randint(1,x)
    guess = 0
    guess= int(input("guess the no.:"))
    while guess != cans:
        if guess<cans:
            guess=int(input(" too low try again!! "))
        elif guess>cans:
            guess=int(input("too high try again!! "))
    print(f'yay!!{guess} is the correct answer.')
guessit(50)