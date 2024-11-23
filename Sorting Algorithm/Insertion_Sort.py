L = [10, 23, 2, 45, -3, 9, 56, 12]
for ind1 in range(len(L)-1):
    li = ind1
    for ind2 in range(ind1 + 1, len(L)):
        if L[li] > L[ind2]:
            li = ind2
    L[ind1], L[li] = L[li], L[ind1]

print(L)