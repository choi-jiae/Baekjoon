import sys

def queue(instruction, q):
    inst = instruction.split()
    i = inst[0]

    if i == 'push':
        q.append(int(inst[1]))
    elif i == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif i == 'size':
        print(len(q))
    elif i == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif i == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif i == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

input = sys.stdin.readline
q =[]
N = int(input())

for _ in range(N):
    queue(input().strip('\n'), q)