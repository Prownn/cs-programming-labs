a = int(input())
b = int(input())
sum = 0
mult = 1

while a > b:
    a = int(input())
    b = int(input())

for i in range (a, b+1):
    sum += i
    mult *= i
print(sum, mult)
