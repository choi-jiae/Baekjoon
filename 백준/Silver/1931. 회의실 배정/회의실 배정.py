N = int(input())
time = [[0]*2 for _ in range(N)]

for i in range(N):
    start, end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end

def schedule(N, time):
    ### Write your code ###
    # 끝나는 시간이 빨라야 더 많은 수업을 넣을 수 있음
    # 끝나는 시간이 동일한 경우에는 시작 시간이 빠른 순서대로 시간표를 짜야 다음 수업을 더 많이 고려 가능

    time.sort(key = lambda x: x[0]) # 시작 시간이 빠른 순서대로 정렬한 후,
    time.sort(key = lambda x: x[1]) # 끝나는 시간이 빠른 순서대로 정렬
    cnt = 0 # 최대 가능한 수업의 수를 저장
    start = 0 # 현재 가능한 시작 시간

    for t in time:
      
      if t[0]>=start: # 시간표에 넣으려는 수업의 시작 시간이 현재 가능한 시작 시간보다 빠르지 않다면 시간표에 추가
        cnt += 1 # 가능한 수업의 수 업데이트
        start = t[1] # 방금 넣은 수업의 끝나는 시간으로 가능한 시작 시간 업데이트

    return cnt

result = schedule(N, time)
print(result)