# 미션 5: 별표(*)를 활용한 가변 언패킹

# 문제 설명: 리스트 data에는 시험 점수들이 들어있습니다. 가장 낮은 점수와 가장 높은 점수를 제외한 나머지 점수들의 평균을 구하기 위해, 언패킹(*)을
# 사용하여 min_score, mid_scores(리스트), max_score로 데이터를 분리하세요. (단, 데이터는 정렬되어 있다고 가정합니다.)

data = [50, 70, 80, 90, 100]

min_score, *mid_scores, max_score = data

print(f"min={min_score}, mid={mid_scores}, max={max_score}")