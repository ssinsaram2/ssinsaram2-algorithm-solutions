# 미션 4: 범위 반복문 활용(for loop & range)

# 문제 설명: 정수 n이 주어질 때, 1부터 n까지의 모든 정수의 합을 구하여 반환화세요. for 반복문과 range() 함수를 반드시 사용해야 합니다.

n = 10
sum = 0

for n in range(1, n + 1):
    sum += n

print(sum)