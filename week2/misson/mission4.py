# 미션 4: Ternary Operator를 이용한 인라인 조건문

# 문제 설명: 정수 n이 매개변수로 주어집니다. n이 0보다 크면 "Positive", 0이면 "Zero", 0보다 작으면 "Negative"를 반환하는 함수를 작성하세요.
# 일반적인 if~else 블록 대신, 한 줄로 표현 가능한 삼항 연산자(Ternary Operator) 형태를 중첩하여 작성해보세요.
n = -5

answer = "Positive" if n > 0 else ("Zero" if n == 0 else "Negative")

print(answer)