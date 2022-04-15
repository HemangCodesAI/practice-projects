import random
chars ='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./\`<>?;':"[]{}!@#$%^&*()_+-='''
no=int(input('Enter number of passwords you want to generate:'))
length=int(input('Enter length of passwords: '))
for pwd in range(no):
    passwords =''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)