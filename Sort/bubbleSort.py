def bubbleSort(A):
	for numElements in range(len(A), 0, -1):
		for i in range(numElements-1):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
	#return A

def bubbleSort(A):
    print("초기 배열:", A)
    for numElements in range(len(A), 0, -1):
        print(f"\n{'=' * 40}")
        print(f"외부 루프: {len(A) - numElements + 1}번째 패스")
        swap_occurred = False
        for i in range(numElements-1):
            print(f"\n현재 상태: {A}")
            print(f"비교: {A[i]} > {A[i+1]}?", end=" ")
            if A[i] > A[i+1]:
                print("예, 교환")
                A[i], A[i+1] = A[i+1], A[i]
                swap_occurred = True
            else:
                print("아니오, 유지")
        if not swap_occurred:
            print("\n더 이상 교환이 없습니다. 정렬 완료!")
            break
    print("\n최종 정렬된 배열:", A)
    return A