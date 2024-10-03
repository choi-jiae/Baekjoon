nlist = list(map(int, input().split()))

a, b = max(nlist), min(nlist)

def getMaxi(a, b):
    while True:
        if a%b == 0:
            return b
        else:
            a, b = b, a%b
            
maxi = getMaxi(a, b)
mini = int(a * (b/maxi))

print(maxi)
print(mini)