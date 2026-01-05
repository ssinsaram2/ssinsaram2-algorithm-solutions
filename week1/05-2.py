# 05-2. 리스트의 동적 관리와 시간 복잡도

# 리스트 기본 조작 및 효율성
numbers = []

numbers.append(10)      # 리스트 끝에 추가: O(1) - 매우 빠름
numbers.append(20)
numbers.append(30)

# 특정 위치의 데이터 삭제 및 반환
last_item = numbers.pop()   # 30 추출: O(1)

# 리스트의 길이 확인
current_size = len(numbers) # 2: O(1) - 파이썬은 길이를 따로 저장해 둠

# 인덱싱과 슬라이싱
print(f"첫 요소: {numbers[0]}, 마지막 요소: {numbers[-1]}")
