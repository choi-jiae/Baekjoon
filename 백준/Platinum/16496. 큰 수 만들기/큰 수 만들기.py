def max_num(N, nums):
  str_nums = [str(num) for num in nums]
  str_nums.sort(reverse = True, key=lambda x: x[0])

  for i in range(N-1, 0, -1):
    for j in range(i):
      first = str_nums[j]
      second = str_nums[j+1]

      if int(first+second) < int(second+first):
        str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]

  result = ''
  for i in range(N):
    result += str_nums[i]

  return int(result)

N = int(input())
nums = list(map(int, input().split()))

answer = max_num(N, nums)
print(answer)