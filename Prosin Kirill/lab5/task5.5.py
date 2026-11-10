c = 0
sum = 0
while True:
    num = input()
    if num == "stop":
        break
    c += 1
    sum += float(num)
print(f"Покупок: {c} \n Общая стоимость: {int(sum)} руб \n Средняя стоимость: {sum/c} руб")
