N = int(input())

isPossible = False

for five in range(N//5, -1, -1):
    total = five
    if (N-5*five)%3 == 0:
        total += (N-5*five)//3
        isPossible = True
        break

if isPossible:
    print(total)
else:
    print(-1)