from array_maker import ArrayMaker

A = ArrayMaker.make_array(10)
# alg
for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i > -1 and A[i] < key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
print(A)
