import collections

def solution(clothes):
    
    types = [x[1] for x in clothes]
    types_num = collections.Counter(types)
    
    answer = 1
    for t in types_num:
        answer =  answer * (types_num[t] + 1)
    
    
    return answer -1