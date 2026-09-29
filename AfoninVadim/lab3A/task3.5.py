from curses.ascii import *
text = str(input())
print(f'''
Длина: {len(text)}
Только буквы: {text.isalpha()}
Только цифры: {isdigit(text)}
Буквенно-цифровая: {isalnum(text)}
Содержит дефис: {'-' in text}
''')
