N, M = map(int, input().split())
nums = [str(i) for i in range(1, N*M+1)]

for n in range(N):
    print(' '.join(nums[n*M:(n+1)*M]))