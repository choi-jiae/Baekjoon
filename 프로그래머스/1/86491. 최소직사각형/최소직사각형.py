# 명함 길이가 긴 쪽을 무조건 가로로 생각
def solution(sizes):
    max_w = 0
    max_h = 0
    for s in sizes:
        w = max(s[0], s[1])
        h = min(s[0], s[1])
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    answer = max_w * max_h
    return answer