# 02-1. 명시적 현 변환의 필수성

# 사용자의 입력을 정수로 변환하는 예시
raw_input = "25"			# 문자열 데이터
age = int(raw_input)		# 정수형으로 명시적으로 변환
next_year_age = age + 1		# 이제 산술 연산이 가능함

# 수치형 사이의 변환
pi = 3.14159
integer_pi = int(pi)		# 소수점 아래를 버리고 정수 3만 취함
print(f"정수 변환 결과: {integer_pi}")
