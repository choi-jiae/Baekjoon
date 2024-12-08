x_points = {}
y_points = {}
for i in range(3):
    a, b = map(int, input().split())
    if a in x_points:
        x_points[a] += 1
    else:
        x_points[a] = 1
    if b in y_points:
        y_points[b] += 1
    else:
        y_points[b] = 1

a, b = 0, 0
for x in x_points:
    if x_points[x] == 1:
        a = x
for y in y_points:
    if y_points[y] == 1:
        b = y
print(a, b)
