import heapq

def card_sort():
    N = int(input()) # 카드 묶음의 개수
    cards = [] # 카드 묶음의 각각의 크기를 list에 저장
    result = 0 # 비교 횟수
    for _ in range(N):
      heapq.heappush(cards, int(input()))

    # 카드 묶음의 크기 중 가장 작은 크기의 묶음 두 개를 합치는 작업을
    # 카드 묶음이 한 묶음 남을 때까지 반복
    while len(cards)>1:
      small_1 = heapq.heappop(cards)
      small_2 = heapq.heappop(cards)

      result += small_1 + small_2
      heapq.heappush(cards, small_1+small_2)

    return result
result = card_sort()
print(result)