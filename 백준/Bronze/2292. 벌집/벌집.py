N = int(input())

rooms = 1
floor = 1

if N == 1:
    print(rooms)
else:
    while N > 1:
        rooms += 1
        N -= 6*floor
        floor += 1

    print(rooms)