import sys
input = sys.stdin.readline

M = int(input())

my_set = 0b0

for m in range(M):
    inst = input().strip('\n')
    inst_list = list(map(str, inst.split()))
    op = inst_list[0]
    if len(inst_list) > 1:
        num = int(inst_list[1])

    if op == 'add':
        my_set = my_set | (1 << num)
    
    elif op == 'remove':
        my_set = my_set & ~( 1 << num)

    elif op == 'check':
        if my_set & ~(1 << num) == my_set:
            print(0)
        else:
            print(1)
    
    elif op == 'toggle':
        my_set = my_set ^ (1 << num)

    elif op == 'all':
        my_set = (1 << 21)-1
    
    elif op == 'empty':
        my_set = 0