M, N = map(int,input().split())

num_list = [1 for _ in range(N+1)]

num_list[0] = 0
num_list[1] = 0

for i in range(2, N+1):
    if num_list[i] == 1:
        for idx in range(i*2, N+1, i):
            num_list[idx] = 0

for i, n in enumerate(num_list):
    if n == 1 and i>=M:
        print(i)