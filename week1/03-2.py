# 03. 연산자 체계와 연산 효율성(operatons)
# 03-2. 논리 연산과 단락 평가(Short-circuit Evaluation)

# 단락 평가의 실전 사례
def check_status():
    print("시스템 상태 확인 중...")
    return True

# list_a가 비어있지 않을 때만 두 번째 조건을 확인하므로 에러를 방지함
items = []

if items and check_status():
    print("아이템이 존재하여 시스템이 정상입니다.")
else:
    print("아이템이 없거나 확인을 생락했습니다.")       # check_status()는 실행조차 안 됨
