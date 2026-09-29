word = input()
print(f"""
    Длина: {len(word)}
    Только буквы: {word.isalpha()}
    Только цифры: {word.isdigit()}
    Буквенно-цифровая: {word.isalnum()}
    Содержит дефис: {"-" in word}
    """)