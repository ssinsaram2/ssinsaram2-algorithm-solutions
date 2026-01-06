# 02-2. 중첩 삼항 연산자(Ternary Operator)의 가독성

# [실전 예시] 수치 데이터의 삼항 조건 판별
n = 0

# 구조: [참일 때의 값] if [조건] else [거짓일 때의 값]
# 아래와 같이 중첩하여 다중 분기(Positive / Zero / Negative) 처리 가능
status = "Positive" if n > 0 else ("Zero" if n == 0 else "Negative")

print("\n--- 2.2 삼항 연산자 결과 ---")
print(f"숫자 {n}의 상태 판별: {status}")