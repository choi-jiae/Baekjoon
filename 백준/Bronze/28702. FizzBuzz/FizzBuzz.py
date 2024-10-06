import sys
s_list = []

for _ in range(3):
    s_list.append(sys.stdin.readline().strip())

isDigit = False
digit_idx = -1

for i, s in enumerate(s_list):
    if not (s in ["Fizz", "Buzz", "FizzBuzz"]):
        isDigit = True
        digit_idx = i
        break

if isDigit:
    result = int(s_list[i])+3-i
    if result%15 == 0:
        print("FizzBuzz")
    elif result%3 == 0:
        print("Fizz")
    elif result%5 == 0:
        print("Buzz")
    else:
        print(result)
else:
    if s_list[2] == "Fizz": # 3
        print("4")
    elif s_list[2] == "Buzz": # 5
        print("Buzz")
    else:
        print("16")