N, M = map(int, input().split())
result = []
for n in range(N):
    result.append(list(map(int, input().split())))

for n in range(N):
    line = list(map(int, input().split()))
    for i, l in enumerate(line):
        result[n][i] += l

for r in result:
    for e in r:
        print(e, end=' ')
        