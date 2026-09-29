text = str(input())
text = text.replace(',', '').split(' ')
result = '/'.join(text)
print(result)
