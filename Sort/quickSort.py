def quickSort(A, p:int, r:int):
	if p < r:
		q = partition(A, p, r)	 # 분할
		quickSort(A, p, q-1)	 # 왼쪽 부분 리스트 정렬
		quickSort(A, q+1, r)	 # 오른쪽 부분 리스트 정렬

def partition(A, p:int, r:int) -> int:
	x = A[r]					# x: 기준 원소
	i = p-1					# i: 1구역의 끝 지점
	for j in range(p, r):	# j: 3구역의 시작 지점
		if A[j] < x:
			i += 1
			A[i], A[j] = A[j], A[i]  # 교환
	A[i+1], A[r] = A[r], A[i+1]	   # 기준 원소와 2구역 첫 원소 교환
	return i+1

# 코드 9-5

def quickSort(A, p: int, r: int, depth=0):
    if p < r:
        print(f"{'  ' * depth}퀵 정렬 호출: {A[p:r+1]}")
        q = partition(A, p, r, depth)
        print(f"{'  ' * depth}분할 후: {A[p:r+1]}, 피벗 위치: {q}")
        quickSort(A, p, q - 1, depth + 1)
        quickSort(A, q + 1, r, depth + 1)
    return A

def partition(A, p: int, r: int, depth) -> int:
    x = A[r]  # 피벗
    i = p - 1  # i: 1구역의 끝 지점
    print(f"{'  ' * depth}파티션 시작: 피벗 = {x}")
    print(f"{'  ' * depth}초기 상태: {A[p:r+1]}")
    
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
            print(f"{'  ' * depth}교환: {A[i]} <-> {A[j]}")
            print(f"{'  ' * depth}현재 상태: {A[p:r+1]}")
    
    A[i + 1], A[r] = A[r], A[i + 1]
    print(f"{'  ' * depth}피벗 교환: {A[i+1]} <-> {A[r]}")
    print(f"{'  ' * depth}파티션 결과: {A[p:r+1]}")
    return i + 1