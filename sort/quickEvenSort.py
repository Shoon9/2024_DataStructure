def quickEvenSort(A, p, r):
    if p < r:
        q, t = partitionEven(A, p, r)
        quickEvenSort(A, p, q - 1)
        quickEvenSort(A, t + 1, r)

def partitionEven(A, p, r):
    x = A[r]
    i = p - 1
    j = r
    k = p

    while k < j:
        if A[k] < x:
            i += 1
            A[i], A[k] = A[k], A[i]
            k += 1
        elif A[k] > x:
            j -= 1
            A[k], A[j] = A[j], A[k]
        else:
            k += 1

    A[j], A[r] = A[r], A[j]
    return i + 1, j

