# 미션 2: 데이터 묶기(zip & unpacking)

# 문제 설명: 학생들의 이름이 담긴 리스트 names와 점수가 담긴 리스트 scores가 주어집니다. 인덱스가 같은 이름과 점수를 짝지어 {'이름': 점수} 형태의
# 딕셔너리로 변환하여 반환하세요.

names = ['철수', '영희', '민수']
scores = [90, 85, 70]

result = dict(zip(names, scores))

print(result)