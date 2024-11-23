def linear(L,target,ind = 0):
    for ind in range(len(L)):
        if L[ind] == target:
            return ind
    return -1
    return linear(L, target, ind + 1)
L = [10,18,12,18,28,96]
target = 12
print(linear(L, target))