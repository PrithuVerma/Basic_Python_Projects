def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

opp = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
ask = False
while not ask:
    
    num1 = float(input('Type the first number :\n'))
    for i in opp:
        print(i)
    opp_sym= input('Pickout an operation from the above : \n')
    num2 = float(input('Type the second number :\n'))

    if opp_sym == '+':
        answer = add(num1,num2)
    elif opp_sym == '-':
        answer = subtract(num1,num2)
    elif opp_sym == '*':
        answer = multiply(num1,num2)
    elif opp_sym == '/':
        answer = divide(num1,num2)
    print(f'{num1} {opp_sym} {num2} = {answer}')
    conti = input('Type "yes" for continuing with same number and "no" to create a new calculation :\n')
    if conti.lower() == 'yes':
        ask = False
        
        opp_sym= input('Pick an operation : \n')
        num3 = float(input('Type the third number :\n'))
        cal = opp[opp_sym]
        answer2 = cal(answer,num3)
        print(f'{answer}{opp_sym}{num3} = {answer2}')

    elif conti.lower() == 'no':
        ask = True
