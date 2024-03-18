# 입력
N = int(input())

tips = []
for _ in range(N):
  tips.append(int(input()))

# 정렬(오름차순)
sorted_tips = sorted(tips)

# 정렬(내림차순)
reverse_sorted_tips = sorted(tips, reverse=True)

# 최대 팁 계산
max_tip1 = 0
max_tip2 = 0

for i in range(N):
  if sorted_tips[i]-i > 0:
    max_tip1 += sorted_tips[i]-i
  
  if reverse_sorted_tips[i]-i > 0:
    max_tip2 += reverse_sorted_tips[i]-i
  
if max_tip1 > max_tip2:
  max_tip = max_tip1
else:
  max_tip = max_tip2

print(max_tip)