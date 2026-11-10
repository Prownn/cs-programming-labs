a = int(input())
b = int(input())
gdc = 0

if a <= 0 or b <= 0:
    print('Ошибка')
else:
    while b > 0:
        a, b = b, a % b
print(a)
