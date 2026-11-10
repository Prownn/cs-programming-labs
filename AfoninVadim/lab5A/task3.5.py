n = int(input("Enter a number: "))

greater = 0
lesser = 0
equal_to = 0

for i in range(n):
    if n != 0:
        n2 = float(input("Enter a number 2: "))
        if n2 > 0:
            greater += 1
        elif n2 == 0:
            equal_to += 1
        elif n2 < 0:
            lesser += 1

print(f'Ниже нуля: {lesser}\nРавны нулю: {equal_to}\nВыше нуля: {greater}')
