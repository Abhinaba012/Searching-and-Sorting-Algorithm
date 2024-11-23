L = [6, 7, 10, 11, 19, 30, 50, 70]
target = 32
low = 0
high = len(L) - 1
while low <= high and L[low]<=target<=L[high]:
    ind = int(low + (((high -low) / (L[high] - L[low])) * (target - L[low])))
    if target > L[ind]:
        low = ind + 1
    elif target < L[ind]:
        high = high - 1
    elif target == L[ind]:
        print(ind)
        break
else:
    print(-1)