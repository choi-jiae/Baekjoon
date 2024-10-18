N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

n_dic = {}

for n in n_list:
    if n in n_dic:
        n_dic[n] += 1
    else:
        n_dic[n] = 1

for m in m_list:
    if m in n_dic:
        print(n_dic[m], end=' ')
    else:
        print(0, end=' ')