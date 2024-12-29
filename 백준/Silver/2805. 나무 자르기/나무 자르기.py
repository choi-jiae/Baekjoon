N, M = map(int, input().split())
woods = list(map(int, input().split()))
woods = sorted(woods)

first = 0
last = woods[-1]

while first <= last:
    mid = (first+last)//2

    total = 0

    for w in woods:
        if (w - mid) > 0:
            total += w - mid
        
    if total >= M:
        first = mid + 1
    elif total < M:
        last = mid - 1

print(last)
