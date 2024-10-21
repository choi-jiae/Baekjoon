import sys

input = sys.stdin.readline

def round(num):
    if num - int(num) >=0.5:
        return int(num)+1
    else:
        return int(num)
    
n = int(input())

if n != 0:
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))

    del_n = round(n*0.15)
    sorted_n_list = sorted(n_list)
    result = round(sum(sorted_n_list[del_n:n-del_n])/(n-2*del_n))
else:
    result = 0
print(result)