# 03-2. in 연산자와 집합(Set)의 해시 메커니즘

# [실전 예시] 특정 문자의 포함 여부 판별
vowels = {'a', 'e', 'i', 'o', 'u'}      # 리스트가 아닌 집합(Set)으로 선언
target_word = "apple"

# 집합에 대한 'in' 연산은 매우 빠름
contains_vowel = any(char in vowels for char in target_word)

print("\n--- 3.2 멤버십 테스트 결과 ---")
print(f"'{target_word}'에 모음 포함 여부: {contains_vowel}")

