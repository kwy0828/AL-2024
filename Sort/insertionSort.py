def insertionSort(A):
	for i in range(1, len(A)):
		loc = i-1
		newItem = A[i]
		while loc >= 0 and newItem < A[loc]:
			A[loc+1] = A[loc]
			loc -= 1
		A[loc+1] = newItem

# 코드 9-3

def insertionSort(A):
    print("초기 배열:", A)
    for i in range(1, len(A)):
        print(f"\n{'=' * 40}")
        print(f"외부 루프: {i}번째 요소 삽입")
        loc = i - 1
        newItem = A[i]
        print(f"현재 삽입할 요소: {newItem}")
        print(f"현재 배열 상태: {A}")
        while loc >= 0 and newItem < A[loc]:
            print(f"비교: {newItem} < {A[loc]}? 예, 이동")
            A[loc + 1] = A[loc]
            loc -= 1
            print(f"이동 후 배열 상태: {A}")
        if loc == i - 1:
            print(f"비교: {newItem} < {A[loc]}? 아니오, 유지")
        A[loc + 1] = newItem
        print(f"삽입 후 배열 상태: {A}")
    print("\n최종 정렬된 배열:", A)
    return A