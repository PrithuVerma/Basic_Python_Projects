import random

print('Welcome to the number guessing game ')
print('I am guessing a number from 1 to 100 ')

difficulty = input("Type 'easy' for easy and 'hard' for hard : \n")
lives = []

if difficulty.lower()=='easy':
    lives = 10
elif difficulty.lower()=='hard':
    lives = 5
guess = 0


def check(guess,num):

    if guess > num:
        lives -= 1  
        print('Too High ')
    elif guess < num:
        lives -= 1
        print('Too low ')
    else :
        print(f'You won the number is {num}')


num = random.randint(1,100)
while guess != num:
    guess = int(input('Guess a number  \n'))

check(guess,num)


