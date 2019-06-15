import random

r = random.randint(1, 100)
while True:
    num = input('please guess a number: ')
    num = int(num)
    if num == r:
        print('bingo! congratulations!')
        break
    elif num > r:
        print('your guess is bigger than the target')
    else:
        print('your guess is smaller than the target')

