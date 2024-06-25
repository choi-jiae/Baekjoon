# 여벌 체육복을 가져온 학생도 도난 당할 수 있음
def solution(n, lost, reserve):
    
    # 여벌 체육복을 가져온 학생이 도난 당한 경우 고려 (자기 자신에게 빌려간다고 생각)
    total_lost = list(set(lost)-set(reserve))
    total_reserve = list(set(reserve)-set(lost))
    total_lost.sort()
    
    # 인덱스가 아니니까 1,n의 경우 고려하지 않아도됨!!
    # 순회를 위한 _lost
    _lost = total_lost.copy()
    for l in _lost:
        f = l-1
        b = l+1
        
        if f in total_reserve:
            total_lost.remove(l)
            total_reserve.remove(f)

        elif b in total_reserve:
            total_lost.remove(l)
            total_reserve.remove(b)
        

    answer = n - len(total_lost)
    return answer
