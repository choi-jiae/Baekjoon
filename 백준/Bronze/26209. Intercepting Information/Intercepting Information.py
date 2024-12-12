n_list = list(map(int, input().split()))
error = False
for n in n_list:
    if n == 9:
        error = True
if error:
    print("F")
else:
    print("S")