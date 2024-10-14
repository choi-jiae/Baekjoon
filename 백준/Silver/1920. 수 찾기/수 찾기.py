N = int(input())
a_list = sorted(list(map(int, input().split())))
M = int(input())

num_list = list(map(int, input().split()))

def b_search(left, right, target):
    while left <= right:
    
        mid = (left+right)//2
        if target == a_list[mid]:
            return True
        
        elif target > a_list[mid]:
            left = mid+1
        
        else:
            right = mid-1
    return False

exist_dic = {}
for num in num_list:
    if num in exist_dic:
        print(exist_dic[num])
    else:
        if b_search(0, len(a_list)-1, num):
            exist_dic[num] = 1
            print(1)
        else:
            exist_dic[num] = 0
            print(0)