list = [4, 7, 4, 4, 9]
list1 = []
n = int(input())

for i, j in enumerate(list, start=0):
    if j == n:
        list1.append(i)
print(list1)
