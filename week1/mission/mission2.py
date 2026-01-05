# 미션 2: 산술 연산과 비교(Operators)

# 문제 설명: 두 정수 num1, num2가 주어질 때, 두 수의 합, 차, 곱, 몫(정수 부분)을 순서대로 담은 리스트를 반환하고, 추가로 num1이 num2보다 큰지
# 여부(True/False)를 반환하는 함수를 각각 작성하세요.

num1 = 10
num2 = 3

def num_sum(a, b):
    return a + b

def num_sub(a, b):
    return a - b

def num_mul(a, b):
    return a * b

def num_div(a, b):
    return a // b

def is_bigger(a, b):
    return a > b

answer = []

answer.append(num_sum(num1, num2))
answer.append(num_sub(num1, num2))
answer.append(num_mul(num1, num2))
answer.append(num_div(num1, num2))

print(answer)
print(is_bigger(num1, num2))

