# 선택한 폰켓몬 종류 수의 최댓값
def solution(nums):
    nums_length = len(nums)
    nums_set = set(nums)
    if nums_length//2 < len(nums_set):
        answer = nums_length//2
    else:
        answer = len(nums_set)
    return answer