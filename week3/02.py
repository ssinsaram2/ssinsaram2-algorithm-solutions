# [미션 2] 이름과 점수 리스트를 딕셔너리로 매핑
names = ["철수", "영희", "민수"]
scores = [90, 85, 70]

# zip(names, scores)는 ("철수", 90), ("영희", 85)... 형태의 튜플 쌍을 생성합니다.
# dict() 생성자는 이러한 튜플 쌍을 받아 {키: 값} 형태의 해시 구조로 즉시 변환합니다.
# 이 모든 과정은 단 한 번의 순회(O(N))로 종료됩니다.
student_info = dict(zip(names, scores))

print(f"매핑된 딕셔너리: {student_info}")

# 참고: 특정 학생의 점수를 찾는 속도는 O(1)로 매우 빠릅니다.
print(f"철수의 점수: {student_info['철수']}")