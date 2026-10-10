year = int(input())
if 1 < year < 9999:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный")
    else:
        print("Невисокосный")
else:
    print("Ошибка")
