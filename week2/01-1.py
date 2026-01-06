# 01-1. zip() 함수를 활용한 데이터 결합 및 매핑

# [실전 예시] 두 리스트를 활용한 딕셔너리 일괄 생성
subjects = ["Math", "Science", "History"]
scores = [95, 88, 92]

# dict() 생성자와 zip()을 결합하면 반복문 없이 한 줄로 매핑 가능
# 이는 내부적으로 C로 구현된 최적화 루프를 타게 되어 성능상 유리함
score_dict = dict(zip(subjects, scores))

print("--- 1.1 zip() 활용 결과 ---")
print(f'매핑된 딕셔너리: {score_dict}')
# 결과 {'Math': 95, 'Science': 88, 'History': 92}