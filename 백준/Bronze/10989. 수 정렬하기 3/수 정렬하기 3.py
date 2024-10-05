import sys
N = int(input())

n_dic = {}

for n in range(N):
    num = int(sys.stdin.readline())
    if num in n_dic:
        n_dic[num] += 1
    else:
        n_dic[num] = 1

sorted_dic = sorted(n_dic.items())

for key, value in sorted_dic:
    for v in range(value):
        print(key)