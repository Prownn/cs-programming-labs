number = input("Введите номер телефона в формате +7 (NNN) NNN-NN-NN" )
number = number.replace("-", "").replace(" ", "").replace("+", "").replace("(", "").replace(")", "")
print(number)