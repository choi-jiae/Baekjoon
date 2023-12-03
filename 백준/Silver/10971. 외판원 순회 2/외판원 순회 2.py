n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
graph = [[] for _ in range(n)]
move_cost = float('inf')

for i in range(n):
    for j in range(n):
        if i != j and arr[i][j] != 0:
            graph[i].append((j, arr[i][j]))

def min_cost(x, val, depth, visit, first, graph, n, cost):

    if depth == n: # 모든 마을을 방문한 경우
        for v, c in graph[x]:
          if v == first: # 처음 출발한 마을로의 경로가 존재할 경우 총 val을 계산
              val += c
              cost = min(cost, val) # 이전 cost와 현재 val 중 작은 것으로 cost 업데이트
        return cost # 최소 비용 반환

    for v, c in graph[x]: # 현재 마을에서 갈 수 있는 마을 방문
        if not visit[v] and v != first: # 방문한 적이 없으며, 처음 출발한 마을이 아닌 경우 이동 가능
            visit[v] = True # 방문 표시
            val += c # 이동 비용 업데이트
            cost = min_cost(v, val, depth + 1, visit, first, graph, n, cost) #dfs
            visit[v] = False # 이전 방문 상태로 돌려 놓기
            val -=c

    return cost

for i in range(n):
    visit = [False] * n
    first = i
    result = min_cost(i, 0, 1, visit, first, graph, n, move_cost)

print(result)