text = "www.GOOGLE.com"

# 문자열 길이
print(len(text))

# 첫 문자 대문자로 변경
txt_capitalize = text.capitalize()
print(txt_capitalize)

# 문자열 전체를 대문자로 변경
txt_upper = text.upper()
print(txt_upper)

# 문자열 전체를 소문자로 변경
txt_lower = text.lower()
print(txt_lower)

# 해당 문자가 있는 개수
g_cnt = text.count('G')
print(g_cnt)

# 해당 문자가 있는 위치
g_find = text.find('G')
print(g_find)
g_rfind = text.rfind('G')
print(g_rfind)

# 해당 문자가 있는 위치
g_index = text.index('G')
print(g_index)
g_rindex = text.rindex('G')
print(g_rindex)

# find와 index의 차이
# find의 경우 존재하지 않는 문자가 할당받는 경우 -1을 반환
# index의 경우 존재하지 않는 문자가 할당받는 경우 에러 발생

# 문자열 교체
text_naver = text.replace("GOOGLE", "NAVER")
print(text_naver)

# 문자열 분류 문자 설정
# .을 기준으로 문자를 slice하여 리스트로 저장
print(text.split('.'))

# 문자열의 공백 제거
text = "           www.GOOGLE.com        "
stp = text.strip()
print(stp)
