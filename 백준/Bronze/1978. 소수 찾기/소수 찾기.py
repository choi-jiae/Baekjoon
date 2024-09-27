N = int(input())
numbers = list(map(int, input().split()))

result = 0
for n in numbers:
    isDecimal = True
    for i in range(2, n):
        if n%i == 0:
            isDecimal = False
            break
    if isDecimal and n != 1:
        result += 1
        
print(result)