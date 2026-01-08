# [미션 3] 중복 제거 및 효율적 교집합 찾기
listA = [1, 5, 2, 3]
listB = [2, 3, 4, 5, 9]

# 1. 리스트를 set으로 변환하는 과정에서 중복이 제거되고 해시 태이블이 구축됩니다.
setA, setB = set(listA), set(listB)

# 2. '&' 연산자는 집합의 교집합(Intersection)을 의미합니다.
# 내부적으로 한 집합의 요소를 꺼내 다른 집합의 해시 테이블에서 광속으로 검색합니다.
common_elements = setA & setB

# 3. 결과로 정렬된 리스트로 변환하여 반홥합니다.
result = sorted(list(common_elements))

print(f"공통 요소 확인: {result}")