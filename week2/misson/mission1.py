# 미션 1: zip을 활용한 데이터 매핑

# 문제 설명: 과목명이 담긴 리스트 subjects와 해당 과목 점수가 담긴 리스트 scores가 주어집니다. fo문으로 하나씩 채워 넣는 대신, zip() 함수를 활용하여
# {'과목명': 점수} 혀앹의 딕셔너리를 한 줄로 생성하세요.

subjects = ['Math', 'Sci']
scores = [90, 80]

answer = dict(zip(subjects, scores))

print(answer)