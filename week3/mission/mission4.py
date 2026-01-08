# 미션 4: 문자열 빈도수 계산기

# 문제 설명: 문자열 s가 주어졌을 때, 각 문자가 몇 번 등장하는지 세어 {'문자': 등장 횟수} 형태의 딕셔너리로 반환하세요. collections 모듈의 기능을
# 활용하면 더 간단하게 구현할 수 있습니다.

from collections import Counter

s1 = "banana"
s2 = "mississippi"

print(dict(Counter(s1)))
print(dict(Counter(s2)))