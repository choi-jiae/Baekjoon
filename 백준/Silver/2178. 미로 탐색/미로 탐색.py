from collections import deque

N, M = map(int, input().split())
maze = []
for _ in range(N):
  row = list(map(int, input()))
  maze.append(row)

move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]


def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      new_x = x + move_x[i]
      new_y = y + move_y[i]

      if (new_x < 0 or new_x >= N) or (new_y < 0 or new_y >= M):
        continue
      else:
        if maze[new_x][new_y] == 1:
          maze[new_x][new_y] = maze[x][y] + 1 # 최단거리 누적 기록
          queue.append((new_x, new_y))
  return maze[N-1][M-1]


print(bfs(0,0)) # 원래 (1, 1)이지만, 편의상 (0, 0)