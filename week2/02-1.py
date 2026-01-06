# 02-1. join() 메소드와 불변 객체의 메모리 전략

# [실전 예시] 리스트 태부 단어들을 문장으로 결합
words = ["Python", "is", "a", "powerful", "language"]

# 구분자(Seperator)인 공백 " "을 기준으로 join() 호출
# 이는 가독성뿐만 아니라 성능 면에서도 코딩 테스트의 필수 기술임
sentence = " ".join(words)

print("\n--- 2.1 join() 활용 결과 ---")
print(f"결합된 문장: {sentence}")
