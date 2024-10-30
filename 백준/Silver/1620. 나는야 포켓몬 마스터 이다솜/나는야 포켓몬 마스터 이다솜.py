import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmon_list = []
poketmon_dic = {}
for n in range(N):
    pk = input().strip('\n')
    poketmon_list.append(pk)
    poketmon_dic[pk] = n + 1

for m in range(M):
    q = input().strip('\n')

    if q.isdigit():
        print(poketmon_list[int(q)-1])
    else:
        print(poketmon_dic[q])