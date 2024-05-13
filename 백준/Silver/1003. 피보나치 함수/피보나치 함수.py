T = int(input())
N = []
for _ in range(T):
  N.append(int(input()))

# N = 0 or 1 일 때 호출횟수 저장(0 출력횟수, 1출력횟수)
call_count = [[0, 0] for _ in range(41)]
call_count[0] = [1, 0]
call_count[1] = [0, 1]

for i in range(2, max(N)+1):
  call_count[i] = [call_count[i-1][0]+call_count[i-2][0], call_count[i-1][1]+call_count[i-2][1]]

for n in N:
  print(call_count[n][0], call_count[n][1])