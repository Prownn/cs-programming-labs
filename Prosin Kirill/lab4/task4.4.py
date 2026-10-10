side1 = int(input())
side2 = int(input())
side3 = int(input())

a = side1 < 0 or side2 < 0 or side3 < 0
b = (side1 + side2 <  side3) or (side1 + side3 < side2) or (side2 + side3 < side1)
if a or b:
    print("Треугольник не существует")
else:
    if side1 == side2 == side3:
        print("Равносторонний")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Равнобедренный")
    else:
        print("Разносторонний")
