num = int(input("Enter a number: "))

if num < 2:
    print('Не простое')
else:
    prime = True
    divider = 2
    while divider**2 <= num:
        if num & divider == 0:
            prime = False
            break
        divider += 1
    if prime:
        print('Простое')
    else:
        print('Не простое')
