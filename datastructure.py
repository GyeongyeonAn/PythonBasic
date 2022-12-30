# Dictionary : key와 value가 쌍을 이루는 자료구조
people = {
    "name": "김개똥",
    "phone": "010-2344-1231"
}

print(people["name"], people["phone"])

# key :
# 1. 유일한 값이어야 한다.
# 2. 튜플은 키값으로 이용 가능하다.
# 3. 딕셔너리나 리스트 같은 경우는 사용할 수 없다.
# 4. True와 1, False와 0을 key값으로 같이 설정하는 것은 가급적 피하자
# value :
# 모든 타입을 사용할 수 있다.
books = {
    "Daniel Pink": ["파는 것은 인간이다.", "언제 할 것인가"],
    "Eric Schidt": "새로운 디지털 시대",
    1: "One",
    True: "Yes",
    False: "True"
}

print(books["Daniel Pink"])

# 둘다 값이 Yes로 출력되는 문제 발생
print(books[1])
print(books[True])

coffee = {
    "Java": 2500,
    "Americano": 2500,
    "Latte": 3000
}

# 요소 변경
coffee["Java"] = 3000
print(coffee)

# 요소 추가
coffee["Moka"] = 3000
print(coffee)

# 요소 삭제
del coffee["Java"]
# coffee.pop("Java")
print(coffee)

# 요소 검색
print(coffee["Americano"])
print(coffee.get("Americano"))

# 모든 key 종류 출력
print(coffee.keys())

# 모든 value값 출력
print(coffee.values())

# 모든 key와 value를 튜플 리스트로 변환
print(coffee.items())

# key값이 존재하는가? 반환 값 True or False
print("Moka" in coffee)
