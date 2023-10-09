n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

def fill(n, k, thing, d):
    for i in range(1, n+1):
        for j in range(1, k+1):
            #### Your Code Here ####
            input_w = thing[i][0] # 지금 넣을 물건(i번째 물건)의 무게
            input_v = thing[i][1] # 지금 넣을 물건(i번째 물건)의 가치

            if input_w <= j: # 지금 넣을 물건의 가치가 최대 무게보다 작거나 같을 때
                # 지금 넣을 물건을 넣지 않고 이전번째 물건까지만 고려했을 때의 가치를 유지하는 경우, 지금 넣을 물건을 넣었을 경우
                # 두 경우 중 가치가 큰 쪽을 선택
                d[i][j] = max(d[i-1][j], d[i-1][j-input_w]+input_v)

            else:  # 지금 넣을 물건의 가치가 최대 무게보다 클 때
                d[i][j] = d[i-1][j] # 지금 넣을 물건을 넣지 않고 이전번째 물건까지만 고려했을 때의 가치를 유지



    return d[n][k] # 최대 무게가  k인 가방일 때, n번째 물건까지 고려한 경우의 최대 가치

result = fill(n, k, thing, d)
print(result)