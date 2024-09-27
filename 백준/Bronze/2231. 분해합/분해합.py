N = int(input())

found = False
for num in range(1, N):
    total = num + sum(map(int, str(num)))
    
    if total == N:
        found = True
        print(num)
        break

if not found:
    print(0)