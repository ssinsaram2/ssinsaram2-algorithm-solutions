# 미션 5: 문자열 포맷팅과 인덱싱(String Formatting)

# 문제 설명: 이름 name(문자열)과 나이 age(정수)가 주어질 때, f-string을 사용하여 "My name is [name] and I am [age] years old." 형식의
# 문자열을 반환하고, 별도로 name의 첫 번째 글자만 추출하여 반환하세요.

name = "Shin Je Hyeon"
age = 31

answer1 = f"My name is {name} and I am {age} years old."
answer2 = name[0]

answer = []
answer.append(answer1)
answer.append(answer2)

print(tuple(answer))
