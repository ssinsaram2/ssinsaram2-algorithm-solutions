# 04-3. key 인자와 lambda를 이용한 다중 기준 정렬

# [실전 예시] 길이순으로 정렬하되, 길이가 같으면 사전순 정렬
words = ["apple", "no", "banana", "cat"]

# key에 튜플을 반환하는 lambda를 전달하면 (우선순위1, 우선순위2)로 동작함
words.sort(key=lambda x: (len(x), x))

print("\n--- 4.3 커스텀 정렬 결과 ---")
print(f"정렬된 단어 리스트: {words}")