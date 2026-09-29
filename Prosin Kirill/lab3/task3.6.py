text = input("Введите ровно три непустые части пути через запятую без пробелов: ")
text = text.split(",")
text = "/".join(text)
print(text)