import math

T = int(input())

for t in range(T):
    H, W, N = map(int, input().split())
    Y = N%H
    if (Y == 0):
        Y = H
    X = math.ceil(N/H)
    print('%d%02d' %(Y, X))