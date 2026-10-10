year = int(input())

if year > 9999 or year < 1:
    print("Ошибка")
else:
    if (year % 400 == 0) or year % 4 == 0 and year % 100 != 0:
        print('Високосный')
    else:
        print('Невисокосный')
