N = int(input())

found = False
for num in range(1, N):
    total = num
    for n in str(num):
        total += int(n)
    
    if total == N:
        found = True
        print(num)
        break

if not found:
    print(0)