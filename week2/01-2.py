# 01-2. enumerate()를 통한 인덱스 관리의 안정성 확보

# [실전 예시] 특정 목표값의 모든 인덱스 위치 찾기
nums = [1, 2, 3, 2, 1]
target = 2

# enumerate(nums, start=0) 형식을 가지며,
# (index, value) 쌍을 순차적으로 변환함
target_indices = [idx for idx, val in enumerate(nums) if val == target]

print("\n--- 1.2 enumerate() 활용 결과 ---")
print(f"타겟 '{target}'의 위치 리스트: {target_indices}")   # 결과: [1, 3]