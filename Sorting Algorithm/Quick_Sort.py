def Quick(L):
    if len(L) <= 1:
        return L
    pivot = L[0]
    left = [val for val in L[1:] if pivot > val]
    right = [val for val in L[1:] if pivot <= val]
    return Quick(left) + [pivot] + Quick(right)
L = [10, 23, 2, 45, -3, 9, 56, 12]
print(Quick(L) )