a = int(input())
b = int(input())
sum = 0
mult = 1
if a <= b:
    for i in range(a, b+1):
        sum += i
        mult *= i
    print(sum)
    print(mult)
