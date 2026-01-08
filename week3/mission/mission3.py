# 미션 3: 중복 제거 및 교집합 찾기

# 문제 설명: 두 개의 정수 리스트 listA와 listB가 주어집니다. 두 리스트에 공통으로 포함된 숫자들만 찾아서 오름차순으로 정렬된 리스트를 반환하세요.
# (반복문을 사용한 O(N^2) 비교 대신 set 자료구조의 교집합 연산을 활용하세요.)

listA = [1, 5, 2, 3]
listB = [2, 3, 4, 5, 9]

common_elements = set(listA) & set(listB)

result = sorted(list(common_elements))

print(result)