L = [10, 23, 2, 45, -3, 9, 56, 12]
for ind1 in range(len(L) - 1):
    for ind2 in range((len(L)-1)-ind1):
        if L[ind2] > L[ind2 + 1]:
            L[ind2], L[ind2 + 1] = L[ind2 + 1], L[ind2]
print(L)