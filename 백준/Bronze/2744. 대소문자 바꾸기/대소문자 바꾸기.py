s = input()
result = ''
for i in s:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()
print(result)