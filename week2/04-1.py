# 04-1. map()과 lambda를 통한 일괄 변환

# [실전 예시] 문자열 형태의 숫자 리스트를 정수 리스트로 변환
str_nums = ["1", "2", "3"]

# map(적용할 함수, 대상 Iterable)
# map 객체를 반환하므로 최종적으로 list() 변환이 필요함
int_nums = list(map(int, str_nums))

print("\n--- 4.1 map/lambda 결과 ---")
print(f"변환된 정수 리스트: {int_nums}")

