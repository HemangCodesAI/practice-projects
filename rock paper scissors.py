import random
def play():
    loop = 0
    computer = 0
    user = 0
    while loop<=10:
        options =('r','p','s')
        comp_choice = random.choice(options)
        user_choice = input('''Press "R" for rock.\nPress "P" for paper.\nPress "S" for scissors.\n''')
        print(f'Computer chose : {comp_choice}\nYou chose : {user_choice}')
        if comp_choice=='s'and user_choice=='p':
            print("Scissors cut paper . COMPUTER WON")
            computer = computer+1
        elif comp_choice=='s'and user_choice=='r':
            print("Rock breaks scissors . YOU WON")
            user =user+1
        elif comp_choice=='r'and user_choice=='p':
            print("Paper covers rock . YOU WON")
            user =user+1
        elif comp_choice=='r'and user_choice=='s':
            print("Rock breaks scissors . COMPUTER WON")
            computer = computer+1
        elif comp_choice=='p'and user_choice=='r':
            print("Paper covers rock . COMPUTER WON")
            computer = computer+1
        elif comp_choice=='p'and user_choice=='s':
            print("Scissors cut paper . YOU WON")
            user =user+1
        else:
            print("It's a tie")
        loop= loop +1
    print(f'''Your Score : {user}\nComputer's Score : {computer}''')
    if user>computer:
        print("YOU WON!!!")
    elif computer>user:
        print("YOU LOST!!!")
    else :
        print("IT'S A TIE")
play()