arr = [4, 7, 4, 4, 9]
num = 4
ind = []
for i, j in enumerate(arr, start = 0):
    if j == num:
        ind.append(i)
print("Индексы:", ind)
