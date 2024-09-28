l = list(map(str, input().split()))

def cal(a, b, s):
    if s == '+':
        return a+b
    elif s == '-':
        return a-b
    elif s == '*':
        return a*b
    else:
        if a*b >= 0:
            return a//b
        else:
            if a < 0:
                return -(-a//b)
            else:
                return -(a//-b)
            
for i in range(0, len(l), 2):
    l[i] = int(l[i])

first = cal(l[0], l[2], l[1])
second = cal(l[2], l[4], l[3])

result1 = cal(first, l[4], l[3])
result2 = cal(l[0], second, l[1])

if result1 < result2:
    print(result1)
    print(result2)
else:
    print(result2)
    print(result1)