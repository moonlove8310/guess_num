import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('please guess a number: ')
    num = int(num)
    if num == r:
        print('bingo! congratulations!')
        print(count, 'time(s) you guessed')
        break
    elif num > r:
        print('your guess is bigger than the target')
    else:
        print('your guess is smaller than the target')
    print(count, 'time(s) you guessed wrong')

