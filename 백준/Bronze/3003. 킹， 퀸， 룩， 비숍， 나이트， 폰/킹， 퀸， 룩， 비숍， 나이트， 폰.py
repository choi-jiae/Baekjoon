right = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))

result = []
for i, r in enumerate(right):
    result.append(str(r-find[i]))

print(' '.join(result))