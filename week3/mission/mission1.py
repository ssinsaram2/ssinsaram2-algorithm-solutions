# 미션 1: 조건에 맞는 데이터 추출

# 문제 설명: 정수로 이루어진 리스트 numbers가 주어집니다. 이 리스트에서 짝수만 골라내고, 골라낸 값들을 제곱하여 새롤운 리스트를 반환하는 함수를 작성
# 하세요. (가능하면 for 반복문 대신 리스트 컴프리헨션을 사용해 한 줄로 구현해 보세요.)

numbers1 = [1, 2, 3, 4, 5, 6]
numbers2 = [1, 3, 5]

answer1 = [n ** 2 for n in numbers1 if n % 2 == 0]
answer2 = [m ** 2 for m in numbers2 if m % 2 == 0]

print(answer1)
print(answer2)
