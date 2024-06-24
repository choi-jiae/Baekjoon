# set이 다른 경우에는 차집합
# set이 같은 경우에는 for 문...?
def solution(participant, completion):
    if set(participant) != set(completion):
        answer = list(set(participant)-set(completion))[0]
    else:
        sorted_participant = sorted(participant)
        sorted_completion = sorted(completion)
        for i, p in enumerate(sorted_participant):
            if p != sorted_completion[i]:
                answer = p
                break
    return answer