n = int(input())

if n < 2:
    print('Ошибка')
else:
    divider = 2
    dividends = []
    while divider <= n:
        if n % divider == 0:
            dividends.append(str(divider))
            n //= divider
        else:
            divider += 1
    print(' '.join(dividends))
