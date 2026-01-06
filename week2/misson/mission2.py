# 미션 2: enumerate를 활용한 조건부 인덱스 찾기

# 문제 설명: 정수 리스트 nums와 목표값 target이 주어집니다. 리스트를 순회하며 target과 일치하는 모든 요소의 인덱스를 리스트에 담화 반환하세요.
# range(len(nums)) 대신 enumerate를 사용하여 구현해야 합니다.

nums = [1, 2, 3, 2, 1]
target = 2

answer = [index for index, val in enumerate(nums) if val == target]

print(answer)
