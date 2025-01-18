import os
while True:
    x = input('What do you want to say : ')
    if x =='q':
        break
    command = f'say {x}'
    os.system(command=command)
    