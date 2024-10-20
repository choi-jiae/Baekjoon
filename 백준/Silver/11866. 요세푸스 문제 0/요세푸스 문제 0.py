N, K = map(int, input().split())

n_list = [n for n in range(1, N+1)]
out_list = []

n_idx = K

while n_list:
    for k in range(K):
        popped = n_list.pop(0)
        n_list.append(popped)
    out_list.append(str(n_list.pop()))

result = '<'+', '.join(out_list)+'>'

print(result)