T = int(input())


def people(k, n):
    p_list = [[0 for _ in range(n)] for _ in range(k+1)]
    p_list[0] = [p for p in range(1, n+1)]

    for floor in range(1, k+1):
        for room in range(n):
            p_list[floor][room] += sum(p_list[floor-1][:room+1])
    return p_list[k][n-1]

for t in range(T):
    k = int(input())
    n = int(input())
    print(people(k, n))