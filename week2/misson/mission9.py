# 미션 9: key를 이용한 커스텀 정렬(문자열 길이)

# 문제 설명: 단어 리스트 words가 주어집니다. 이 단어들을 단어의 길이를 기준으로 오름차순 정렬하세요. 길이가 같다면 사전순으로 정렬해야 합니다. sort()
# 메소드의 key 인자에 lambda를 활용하세요.
words = ["apple", "no", "banana", "cat"]

words.sort(key=lambda x: (len(x), x))

print(words)