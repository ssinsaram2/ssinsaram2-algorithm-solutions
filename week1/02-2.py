# 02. 데이터 형 변환과 예외 처리(Type Casting)
# 02-2. 형 변환시 발생할 수 있는 오류(ValueError)

user_data = "2024년"

try:
	# 숫자가 아닌 문자가 포함되어 있어 에러 발생 가능성이 높음
	converted_data = int(user_data)
except ValueError:
	# 에러 발생 시 프로그램 종료 대신 대체 로직을 수행
	print("수치형 데이터로 변환할 수 없는 형식입니다. 전처리가 필요합니다.")
