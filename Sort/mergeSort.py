def mergeSort(A, p:int, r:int):
	if p < r:
		q = (p+r) // 2
		mergeSort(A, p, q)
		mergeSort(A, q+1, r)
		merge(A, p, q, r)

def merge(A, p:int, q:int, r:int):
	i = p; j = q+1; t = 0
	tmp = [0 for i in range(len(A))]
	while i <= q and j <= r:
		if A[i] <= A[j]:
			tmp[t] = A[i]; t += 1; i += 1
		else:
			tmp[t] = A[j]; t += 1; j += 1
	while i <= q:
		tmp[t] = A[i]; t += 1; i += 1
	while j <= r:
		tmp[t] = A[j]; t += 1; j += 1
	i = p; t = 0
	while i <= r:
		A[i] = tmp[t]; t += 1; i += 1

# 코드 9-4

def mergeSort(A, p: int, r: int, depth=0):
    if p < r:
        q = (p + r) // 2
        print(f"{'  ' * depth}분할: {A[p:r+1]}")
        mergeSort(A, p, q, depth + 1)
        mergeSort(A, q + 1, r, depth + 1)
        merge(A, p, q, r, depth)
    return A

def merge(A, p: int, q: int, r: int, depth):
    print(f"{'  ' * depth}병합 시작: {A[p:q+1]} 와 {A[q+1:r+1]}")
    i = p
    j = q + 1
    t = 0
    tmp = [0 for _ in range(len(A))]
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        t += 1
        i += 1
    print(f"{'  ' * depth}병합 결과: {A[p:r+1]}")