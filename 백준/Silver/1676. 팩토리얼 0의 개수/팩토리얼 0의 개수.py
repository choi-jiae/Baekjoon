N = int(input())

fac = 1
for i in range(2, N+1):
    fac *= i

cnt = 0
for f in str(fac)[::-1]:
    if f != '0':
        break
    else:
        cnt += 1

print(cnt)