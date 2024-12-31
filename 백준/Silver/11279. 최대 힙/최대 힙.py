import sys
input = sys.stdin.readline
N = int(input())
arr = []
def max_heap_input(arr, num):
    arr.append(num)
    child = len(arr)-1
    parent = (child+1)//2-1
    
    while child != 0 and arr[child] >= arr[parent]:
        arr[child], arr[parent] = arr[parent], arr[child]
        child = parent
        parent = (child+1)//2-1
    return arr

def max_heap_delete(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    print(arr.pop())
    
    parent = 0
    child = (parent+1)*2-1 # 왼쪽 자식
    if child < len(arr)-1 and arr[child] < arr[child+1]:
        child += 1
    while child <= len(arr)-1 and arr[child] >= arr[parent]:
        arr[child], arr[parent] = arr[parent], arr[child]
        parent = child
        child = (parent+1)*2-1
        if child < len(arr)-1 and arr[child] < arr[child+1]:
            child += 1
    return arr

for n in range(N):
    inst = int(input())
    if inst == 0:
        if len(arr) == 0:
            print(0)
        else:
            max_heap_delete(arr)
    else:
        max_heap_input(arr, inst)