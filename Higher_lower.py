import random
celebrities = {
    'Cristiano Ronaldo': 342_000_000,
    'Dwayne "The Rock" Johnson': 245_000_000,
    'Ariana Grande': 244_000_000,
    'Kylie Jenner': 243_000_000,
    'Selena Gomez': 231_000_000,
    'Kim Kardashian': 224_000_000,
    'Lionel Messi': 195_000_000,
    'Beyoncé': 182_000_000,
    'Justin Bieber': 179_000_000,
    'Neymar Jr.': 158_000_000
}
def play():
    points = 0
    while True:
        celeb_1 = random.choice(list(celebrities.keys()))
        celeb_2 = random.choice(list(celebrities.keys()))
        f1 = celebrities[celeb_1]
        f2 = celebrities[celeb_2]

        while celeb_1 == celeb_2:
            celeb_2 = random.choice(list(celebrities.keys()))

        print(f"\nWho has more followers on Instagram?")
        print(f"1. {celeb_1}")
        print(f"2. {celeb_2}")

        guess = int(input('Guess which celebrity have more followers, Type "1" and "2" as your answer \n'))

        if guess == 1 and f1 > f2:
            points += 1
            print(f'Correct your score is {points} ')
        elif guess == 2 and f2 > f1 :
            points += 1
            print(f'Correct your score is {points} ')
        else:
            print(f'You loose your final score is {points}')
            break

    play_again= input('Do you want to play again ? y/n')

    if play_again.lower() == 'y':
        play()
    else:
        print('Thank you for playing')

play()
