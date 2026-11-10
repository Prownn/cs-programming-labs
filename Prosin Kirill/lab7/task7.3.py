arr = [int(part) for part in input().split()]
num = int(input())
ind = []
for i, j in enumerate(arr, start = 0):
    if j == num:
        ind.append(i)
print("Индексы:", ind)
