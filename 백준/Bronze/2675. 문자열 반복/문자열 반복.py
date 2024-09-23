T = int(input())
for t in range(T):
    R, S = input().split()
    
    result = ""
    for s in S:
        result += s*int(R)
    print(result)