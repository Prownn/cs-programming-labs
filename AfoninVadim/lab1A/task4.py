sec_input = input("Введите секунды поездки: ")
sec_input = int(sec_input)
hour = sec_input//3600
min = sec_input//60 % 60
sec =  sec_input % 60
print(f'{hour:02d}:{min:02d}:{sec:02d}')