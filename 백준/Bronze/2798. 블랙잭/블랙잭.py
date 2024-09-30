N, M = map(int, input().split())
cards = list(map(int, input().split()))

best = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            total = cards[i]+cards[j]+cards[k]
            if total == M:
                print(total)
                exit(0)
            elif total < M:
                best = max(best, total)
print(best)