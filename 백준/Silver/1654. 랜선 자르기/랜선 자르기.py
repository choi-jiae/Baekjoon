import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lans = []
for _ in range(K):
    lans.append(int(input()))

start = 1
end = max(lans)
length = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for lan in lans:
        cnt += lan//mid
    
    if cnt < N:
        end = mid-1
    else:
        if length < mid:
            length = mid
        start = mid+1

print(length)