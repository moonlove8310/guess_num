import random
start = input('please give a start number to guess range: ')
end = input('please give an end number to guess range: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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

