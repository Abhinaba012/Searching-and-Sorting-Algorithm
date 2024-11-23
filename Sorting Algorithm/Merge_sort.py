l = [1, 13, 45, 23, 34, 6, 12, 33]
def divide(l):
    if len(l) > 1:
        left = l[:len(l) // 2]
        right = l[len(l) // 2 : ]
        divide(left), divide(right)
        conq(l, left, right)
def conq(l, left, right):
    li, ri, ind = 0, 0, 0
    while li < len(left) and ri < len(right):
        if left[li] > right[ri]:
            l[ind] = right[ri]
            ri += 1
        else:
            l[ind] = left[li]
            li += 1
        ind += 1
    while li < len(left):
        l[ind] = left[li]
        li += 1
        ind += 1
    while ri < len(right):
        l[ind] = right[ri]
        ri += 1
        ind += 1

divide(l)
print(l)