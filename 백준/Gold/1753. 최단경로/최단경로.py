import heapq

V, E = map(int, input().split())
K = int(input())

INF = float("inf")
results = [INF for _ in range(V+1)]

graph = [[] for _ in range(V+1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  results[start] = 0
  while q:
    # 가장 최단 거리가 짧은 노드 정보 꺼내기
    dist, now = heapq.heappop(q)
    
    if results[now]<dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]

      if results[i[0]] > cost:
        results[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for result in results[1:]:
  if result == INF:
    print("INF")
  else:
    print(result)