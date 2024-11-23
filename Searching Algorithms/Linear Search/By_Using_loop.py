A = [10,18,12,18,28,96]
target = 18
for ind in range(0, len(A)):
    if A[ind] == target:
        print(ind)
        break
else:
    print(-1)

B = [10,18,12,18,28,96]
target1 = 96
index = 0
while index != len(B):
    if B[index] == target1:
        print(index)
        break
    index += 1
else:
    print(-1)