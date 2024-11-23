def linear(L, target):
    for ind in range(0, len(L)):
        if L[ind] == target:
            return ind
    return -1
L = [10, 12, 14, 15, 10, 14]
target = 12
print(linear(L, target))