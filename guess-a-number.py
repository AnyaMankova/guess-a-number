import random
from math import log2, ceil

def is_valid():
    if 1 <= number <= right_range:
        return True
    else:
        return False


print('Добро пожаловать в числовую угадайку')
print('Укажи правую границу для генерации случайного числа:')
right_range = int(input())
n = random.randint(1, right_range)
print('Загадано число от 1 до', right_range, '!\nВведи своё число:')
number = int(input())
count = 0

while is_valid():
    if number == n:
        print('Вы угадали, поздравляем!\nКоличество попыток -', count)
        print('Минимальное количество попыток для гарантированного угадывания:', int(log2(number)))
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break

    elif number < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        number = int(input())
        count += 1
    else: 
        print('Ваше число больше загаданного, попробуйте еще разок')
        number = int(input())
        count += 1
else:
    print('А может быть все-таки введем целое число от 1 до', right_range, '?')