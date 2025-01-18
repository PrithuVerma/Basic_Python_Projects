alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
direction = input('Type "encode" to encrypt and "decode" to dcrypt \n')
text = input('Type your message :\n')
shift = int(input('Type the number of shifts :\n'))

def encrypt(plain_text,shift_amount):
    new_text = ''
    for i in plain_text:
        position = alphabet.index(i)
        new = position + shift_amount
        letter = alphabet[new]
        new_text += letter
    print(new_text)

def dcrypt(complex_text , shift_amount):
    old_text = ''
    for i in complex_text:
        position = alphabet.index(i)
        old = position - shift_amount
        letter1 = alphabet[old]
        old_text += letter1
    print(old_text)

if direction == 'encode':
    encrypt(plain_text = text , shift_amount = shift)
elif direction == 'decode':
    dcrypt(complex_text = text , shift_amount = shift)
