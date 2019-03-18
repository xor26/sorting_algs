from array_maker import ArrayMaker


def merge_sort(A, p, r):
    if p < r:
        print("merged " + str(p) + " : " + str(r) + " array: " + str(A))

        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    L = []
    for elem in A[p:q+1]:
        L.append(elem)

    R = []
    for elem in A[q+1:r+1]:
        R.append(elem)

    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        if i == len(L)-1 or j == len(R)-1:

            break

A = ArrayMaker.make_array(100)
# A = [1, 4, 5, 6, 8, 2, 3, 7, 9, 10]
# merge(A, 0, 4, 9)
#
# A = [10, 1, 6, 5, 7, 2, 3, 8, 4, 9, 11]

A = [3, 23, 52, 26, 38, 57, 9, 49]
merge_sort(A, 0, len(A)-1)
print(A)
