import random
def deal_cards():

    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

def calculate(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def compare(user_score,comp_score):
    if user_score == comp_score:
        return 'Its a fucking Draw' 
    elif comp_score == 0:
        return'You lose'
    elif user_score == 0:
        return 'You win'
    elif user_score > 21:
        return 'You went overboard, You lose'
    elif comp_score > 21:
        return 'Computer went overboard, You win'
    elif user_score > comp_score:
        return 'You win'
    else:
        return 'You lose'

comp_cards = []
user_cards = []
game_over = False

for _ in range(2):
    comp_cards.append(deal_cards())
    user_cards.append(deal_cards())
while not game_over:
    user_score = calculate(user_cards)
    comp_score = calculate(comp_cards)
    print(f'Your cards: {user_cards},current score : {user_score}')
    print(f"Computer's cards: {comp_cards[0]}")
    
    #User Loop
    if user_score == 0 or comp_score == 0 or user_score > 21:
        game_over = True
    else:
        conti = input('Do you want to continue ? Y/N \n')
        if conti.lower()=='y':
            user_cards.append(deal_cards())
        elif conti.lower()=='n':
            game_over = True
#Comp loop
while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_cards())
    comp_score = calculate(comp_cards)

print(f"Your final hand: {user_cards},final score: {user_score}")
print(f"Computer's final hand: {comp_cards},final score: {comp_score}")
print(compare(user_score,comp_score))