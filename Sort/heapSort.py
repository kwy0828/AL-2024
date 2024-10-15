def heapSort(A):
	buildHeap(A)
	for last in range(len(A)-1, 0, -1):
		A[last], A[0] = A[0], A[last]
		percolateDown(A, 0, last-1)

def buildHeap(A): # 리스트 A[0...len(A)-1]을 힙으로 만든다
	for i in range((len(A)-2) // 2, -1, -1):
		percolateDown(A, i, len(A)-1)

# A[k]를 루트로 하는 서브 트리가 A[k...end] 범위 내에서 힙 특성을 만족하도록 수선
# 주어진 조건: A[k]의 두 자식을 루트로 하는 서브 트리는 힙 특성을 만족함
def percolateDown(A, k:int, end:int):
	child = 2*k+1	 # 왼자식
	right = 2*k+2	 # 오른자식
	if child <= end:
			if right <= end and A[child] < A[right]:
					child = right
			# child: A[2k+1]와 A[2k+2] 중에 큰 원소의 인덱스
			if A[k] < A[child]:
				A[k], A[child] = A[child], A[k]
				percolateDown(A, child, end)

# 코드 9-7

def heapSort(A):
    print("초기 배열:", A)
    buildHeap(A)
    print("\n힙 구축 완료:", A)
    for last in range(len(A)-1, 0, -1):
        print(f"\n최대 원소 {A[0]}를 마지막 위치 {last}로 이동")
        A[last], A[0] = A[0], A[last]
        print("교환 후 배열:", A)
        percolateDown(A, 0, last-1)
    print("\n최종 정렬된 배열:", A)

def buildHeap(A):
    print("\n힙 구축 시작")
    for i in range((len(A)-2) // 2, -1, -1):
        print(f"\n노드 {A[i]} (인덱스 {i})에서 percolateDown 시작")
        percolateDown(A, i, len(A)-1)
        print(f"현재 배열 상태: {A}")

def percolateDown(A, k: int, end: int):
    child = 2*k+1
    right = 2*k+2
    if child <= end:
        if right <= end and A[child] < A[right]:
            child = right
        print(f"  비교: 부모 {A[k]} vs 자식 {A[child]}")
        if A[k] < A[child]:
            print(f"  교환: {A[k]} <-> {A[child]}")
            A[k], A[child] = A[child], A[k]
            print(f"  교환 후 배열: {A}")
            percolateDown(A, child, end)
        else:
            print("  교환 불필요")