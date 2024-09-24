T = int(input())
for t in range(T):
    result = input()
    now_p = 0
    total_p = 0
    for r in result:
        if r == 'O':
            now_p += 1
            total_p += now_p
        else:
            now_p = 0

    print(total_p)