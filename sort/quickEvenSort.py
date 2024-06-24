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

import random

def quickEvenSort2(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickEvenSort2(A, p, q-1)
        quickEvenSort2(A, q+1, r)

def partition_helper(A, p, r):
    i = random.randint(p, r)  # p와 r 사이에서 임의의 인덱스 선택
    A[i], A[r] = A[r], A[i]  # 선택된 피벗을 배열의 끝으로 이동
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]  # 이제 피벗은 배열의 마지막 원소
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

# 배열과 초기 인덱스를 입력하여 함수를 사용할 수 있습니다.



