import sys
input = sys.stdin.readline

N = int(input())
n_list = []
cnt_dic = {}

for _ in range(N):
    num = int(input())
    if num in cnt_dic:
        cnt_dic[num] += 1
    else:
        cnt_dic[num] = 1
    n_list.append(num)


mean = sum(n_list)/N

if mean >= 0:
    if mean - sum(n_list)//N >= 0.5:
        print(int(mean)+1)
    else:
        print(int(mean))
else:
    if mean - int(sum(n_list)/N) <= -0.5:
        print(int(mean)-1)
    else:
        print(int(mean))
    

sorted_n_list = sorted(n_list)
print(sorted_n_list[N//2])


max_cnt = max(cnt_dic.values())

max_nums = []
for key, value in cnt_dic.items():
    if value == max_cnt:
        max_nums.append(key)

if len(max_nums) > 1:
    max_nums.sort()
    print(max_nums[1])
else:
    print(max_nums[0])

print(max(n_list)-min(n_list))