n = int(input())
total = 0
sum = 0
if n < 0:
    print('Ошибка')
else:
    if n == 0:
        total = 1
        sum = 0
    while n > 0:
        n2 = n % 10
        sum += n2
        total += 1
        n //= 10
    print(f'''
Цифр: {total}
Сумма цифр: {sum}
''')
