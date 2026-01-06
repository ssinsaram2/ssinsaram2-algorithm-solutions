# 04-2. 슬라이싱의 Step 인자를 활용한 데이터 정제

# [실전 예시] 특정 규칙(짝수번 인덱스)에 따른 문자 추출
s = "abcdef"

# s[시작:끝:간격] ==> 0번부터 끝까지 2칸 간격으로 추출
even_indexed_chars = s[::2]

print("\n--- 4.2 슬라이싱 Step 결과 ---")
print(f"짝수 인덱스 문자열: {even_indexed_chars}")      # 결과: "ace"