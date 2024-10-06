N, K = map(int, input().split())

top = 1
for i in range(K):
    top *= N-i

bottom = 1
for j in range(1, K+1):
    bottom *= j

print(top//bottom)