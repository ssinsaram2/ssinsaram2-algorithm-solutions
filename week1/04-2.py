# 04-2. 반복문과 range 객체의 성능

# 1부터 100까지의 합 구하기
total_sum = 0

for i in range(1, 101):     # 101은 포함되지 않음에 주의
    total_sum += i

# 2차원 리스트(행렬) 순회 예시
matrix = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    for element in row:
        print(element, end=" ")     # 1 2 3 4 5 6 순차적으로 출력