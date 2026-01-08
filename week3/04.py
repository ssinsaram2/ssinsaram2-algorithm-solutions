from collections import Counter

# [미션 4] 문자열 내 문자 빈도수 계산
s = "banana"

# Counter 클래스는 반복 가느한 객체를 입력 받아 요소별 개수를 세어 딕셔너리 형태로 반환합니다.
# 시간 복잡도: O(N) (문자열을 단 한 번만 훑음)
char_counts = Counter(s)

print(f"문자별 등장 횟수: {dict(char_counts)}")


# [심화] 가장 만힝 등장한 요소 추출하기
# most_common(1)은 가장 빈도가 높은 상위 1개 요소를 반환합니다.
most_frequent = char_counts.most_common(1)
print(f"가장 많이 등장한 문자: {most_frequent[0][0]}")