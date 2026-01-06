# 미션 7: map과 lambda를 활용한 일괄 변환

# 문제 설명: 숫자 모양의 문자열이 담긴 리스트 str_nums를 정수형 리스트로 한번에 변환하세요. for 루프를 사용하지 않고 map() 함수를 활용하여 구현해야
# 합니다.

str_nums = ["1", "2", "3"]

answer = list(map(int, str_nums))

print(answer)