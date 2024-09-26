import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt_bundle = 0
for s in sizes:
    tshirt_bundle += math.ceil(s/T)

print(tshirt_bundle)
print(N//P, N%P)