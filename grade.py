
ppl = {}

ques = False

while ques == False:
    name = input('Enter your name : \n')
    bid = int(input('Enter you bid : \n'))
    ppl[name] = bid
    conti = input('Are there any more bidders ? Y/N \n')
    if conti.lower() == 'n':
        ques = True
        print(f'The winner is {max(ppl)}')
    elif conti.lower() == 'y':
        ques = False
