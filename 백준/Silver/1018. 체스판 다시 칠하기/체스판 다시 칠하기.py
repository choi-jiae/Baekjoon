import sys
N, M = map(int, input().split())

board = []

lt_w = ['WBWBWBWB', 
        'BWBWBWBW',
        'WBWBWBWB', 
        'BWBWBWBW',
        'WBWBWBWB', 
        'BWBWBWBW',
        'WBWBWBWB', 
        'BWBWBWBW',]

lt_b = ['BWBWBWBW',
        'WBWBWBWB', 
        'BWBWBWBW',
        'WBWBWBWB', 
        'BWBWBWBW',
        'WBWBWBWB', 
        'BWBWBWBW',
        'WBWBWBWB',]

new_board = []
cnt_list = []

for n in range(N):
    board.append(sys.stdin.readline().strip())

for i in range(N-7):
    
    for j in range(M-7):
        new_board = []
        for k in range(8):
            new_board.append(board[i+k][j:j+8])
    
        w_cnt = 0
        b_cnt = 0

        for y in range(8):
            for x in range(8):
                if lt_w[y][x] != new_board[y][x]:
                    w_cnt += 1
                
                if lt_b[y][x] != new_board[y][x]:
                    b_cnt += 1
        cnt_list.append(w_cnt)
        cnt_list.append(b_cnt)

print(min(cnt_list))