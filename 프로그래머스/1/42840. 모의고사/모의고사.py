# 1 2 3 4 5 반복
# 2 1 2 3 2 4 2 5 (1,3,4,5 사이에 2 끼워 넣음)
# 33 11 22 44 55 반복
def solution(answers):
    s = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    scores = [0, 0, 0]
    
    for i, a in enumerate(answers):
        for j in range(len(s)):
            if a == s[j][i%len(s[j])]:
                scores[j] += 1
                
    max_score = max(scores)
    answer = [i+1 for i in range(len(scores)) if scores[i] == max_score]
    return answer