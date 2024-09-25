triangle = input()

while triangle != '0 0 0':
    a, b, c = map(int, triangle.split())
    lines = sorted([a, b, c])
    
    if (lines[2])**2 == lines[0]**2 + lines[1]**2:
        print("right")
    else:
        print("wrong")
    triangle = input()