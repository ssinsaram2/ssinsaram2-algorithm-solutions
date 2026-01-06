# 05. 집합 연산을 통한 데이터 비교 및 정제(Set Operations)

# [실전 예시] A 리스트에만 존재하는 고유 원소 추출
list_a = [1, 2, 2, 3]
list_b = [3, 4]

# set으로 변환 시 중복이 제거되며, '-' 연산자로 차집합 수행 가능
unique_to_a = list(set(list_a) - set(list_b))

print("\n--- 5. 집합 연산 결과 ---")
print(f"A에만 존재하는 원소(중복 제거): {unique_to_a}")     # 결과: [1, 2]