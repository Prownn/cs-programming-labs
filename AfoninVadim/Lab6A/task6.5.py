n = int(input())

if not 1 <= n <= 10:
    print('Ошибка')
else:
    for i in range(n):
        row = []
        for j in range(n):
            if i >= j:
                dist = i - j
            else:
                dist = j - i
            row.append(str(dist))
        print(' '.join(row))
