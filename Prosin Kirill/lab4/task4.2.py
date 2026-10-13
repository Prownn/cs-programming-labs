coast = int(input())
age = int(input())

if age < 0 or age > 120:
    print("Ошибка")

if age < 6:
    print(f"{coast * 0:.2f} руб")
elif age < 18:
    print(f"{coast * 0.5:.2f} руб")
elif age < 60:
    print(f"{coast:.2f} руб")
else:
    print(f"{coast * 0.7:.2f} руб")
