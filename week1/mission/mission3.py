# 미션 3: 조건에 따른 로직 분기(if~elif~else)

# 문제 설명: 학생의 점수 score가 정수로 주어질 때, 다음 기준에 따라 학점을 문자열로 반환하는 함수를 작성하세요.
# - 90점 이상: "A"
# - 70점 이상 90점 미만: "B"
# - 70점 미만: "C"

score = 89

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")