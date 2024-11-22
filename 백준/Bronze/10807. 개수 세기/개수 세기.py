n = int(input())
n_list = input().split(' ')
key = input()

cnt = 0

for n in n_list:
    if n == key:
        cnt += 1
print(cnt)