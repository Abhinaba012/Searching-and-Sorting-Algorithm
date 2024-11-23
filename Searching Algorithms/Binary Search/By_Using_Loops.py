L = [-7, -2, 3, 5, 11, 19, 26, 36]
target = -2
low = 0
high = len(L) - 1
while low <= high:
    mid = (low + high) // 2

    if L[mid] < target:
        low = mid + 1

    elif L[mid] > target:
        high = mid -1 
    
    elif L[mid] == target:
        print(mid)
        break
else:
    print(-1)