# 뒤에 있는 것이 앞에 있는 것보다 먼저 끝나면 함께 배포
import math

def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    max_day = days.pop(0)
    num = 1
    while days:
        if days[0] <= max_day:
            days.pop(0)
            num += 1
        else:
            answer.append(num)
            max_day = days.pop(0)
            num = 1
    answer.append(num)
    return answer