import sys
N = int(input())

points = []

for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

sorted_points = sorted(points, key= lambda x : (x[1], x[0]))

for p in sorted_points:
    print(p[0], p[1])