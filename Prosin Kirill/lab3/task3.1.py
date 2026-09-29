text = input()
if len(text) == 13:
    text = text.split("-")
    print(f"""
    Категория: {text[0][0:3]}
    Год: {text[1][0:4]}
    Номер: {text[2][0:4]}
    Обратный номер: {text[2][::-1][0:4]}
    """)
