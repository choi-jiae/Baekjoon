result = [ -1 for _ in range(26)]
word = input()
for i, w in enumerate(word):
    if result[ord(w)-ord('a')] == -1:
        result[ord(w)-ord('a')] = i

for r in result:
    print(r, end=" ")