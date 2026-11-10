count = int(input())
positive = 0
negative = 0
zero = 0
for i in range(count):
    num = float(input())
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("Ниже нуля:", negative)
print("Равны нулю:", zero)
print("Выше нуля:", positive)


