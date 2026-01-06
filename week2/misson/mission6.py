# 미션 6: in 연산자를 활용한 존재 여부 확인

# 문제 설명: 문자열 s가 주어질 때, 해당 문자열에 모음(a, e, i, o, u)이 포함되어 있는지 여부를 판별하는 효율적인 코드를 작성하세요. 여러 번의 or
# 조건문 대신 in 연산자와 집합(set)을 활용하여 파이썬스럽게 구현하세요.

s = "programming"
vowels = {"a", "e", "i", "o", "u"}

answer = any(char in vowels for char in s)

print(answer)