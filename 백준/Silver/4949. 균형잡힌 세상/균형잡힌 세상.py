import sys
input = sys.stdin.readline

def check_text(text):
    stack = []
    for t in text:
        if t == '(' or t == '[':
            stack.append(t)

        elif t == ')':
            if stack:
                top = stack.pop()
                if top == '(':
                    continue
                else:
                    return 'no'
            else:
                return 'no'
        elif t == ']':
            if stack:
                top = stack.pop()
                if top == '[':
                    continue
                else:
                    return 'no'
            else:
                return 'no'

    if len(stack)==0:
        return 'yes'
    else:
        return 'no'

while True:
    text = input().strip('\n')

    if text == '.':
        break
    else:
        print(check_text(text))