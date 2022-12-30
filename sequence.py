
# 리스트
list_a = [1, 2, 3, 4]
list_b = ["a", "b", "c"]
list_c = [True, False]
list_d = [1, "a", True]
print(list_a)
print(list_b)
print(list_c)
print(list_d)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[0])
print(numbers[3:5])
print(numbers[1:])
print(numbers[-3:-1])

list_lan = ["JAVA", "C", "PYTHON", "Go"]
print(list_lan[0][2])
print(list_lan[2][2:4])

list_lan[1] = "C++"
print(list_lan)

list_lan[1:3] = ["C#", "PYTHON3"]
print(list_lan)

# 리스트 요소 개수 출력
print(len(list_lan))

# 리스트 맨 뒤에 새로운 요소 추가
list_lan.append("Ruby")
print(list_lan)

# 리스트 안에 리스트 요소 추가
list_a = [1, 2, 3]
list_lan.append(list_a)
print(list_lan)

# 리스트 요소를 추출하여 리스트 안에 추가
list_lan.extend(list_a)
print(list_lan)

# 문자열을 extend로 추가하는 경우 문자열의 각 문자 하나씩 리스트에 저장됨
list_lan.extend("JavaScript")
print(list_lan)

# 원하는 위치에 데이터를 리스트에 삽입
list_lan.insert(0, "R")
print(list_lan)

# 제일 뒤에 있는 요소를 반환해주고 삭제
print(list_lan.pop())
print(list_lan)

# 원하는 요소 삭제
list_lan.remove("PYTHON3")
print(list_lan)

# 원하는 요소 위치로 삭제
del list_lan[1]
print(list_lan)

# 리스트 오름차순으로 정렬
numbers = [1000, 5000, 160, 100, 20, 3450]
numbers.sort()
print(numbers)

# 리스트 요소 역순으로 변경
numbers.reverse()
print(numbers)

# 리스트 내림차순으로 정렬
numbers.sort(reverse=True)
print(numbers)

names = ["홍길동", "이승철", "김개똥"]
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# 리스트안에 요소 찾기
list_lan = ["Java", "C", "Python", "Go"]
numbers = [1, 200, 3, 50, 5, 77, 7, 55, 9]
print(50 in numbers)
print("C" not in list_lan)
print("Java Script" not in list_lan)

# 2차원 리스트
td_number = [[10, 20, 30], [1, 2, 3]]
print(td_number)
print(td_number[0][1])

# 튜플
numbers = (1, 2, 3, 4)
# 위 튜플은 numbers = 1, 2, 3, 4 표현과 같다.
# 단, 만약 요소가 한개라면 반드시 ()를 붙어줘야 튜플로 선언된다.
print(numbers)
print(numbers + numbers)
print(numbers * 2)

# 2차원, 3차원 튜플
numbers = (1, 2, 3, (4, 5, (6, 7)))
print(numbers)

# 튜플 인덱싱
print(numbers.index(3))

print(numbers[3])

numbers = 1, 2, 3, 4
# *number3는 나머지 요소를 다 넣겠다는 뜻입니다.
number1, number2, *number3 = numbers
print(number1, number2, number3)

# 요소 추가 (원래 튜플은 요소 추가가 안된다)
# 아래 내용은 요소가 추가된 것처럼 보이지만, 사실 다른 주소로 튜플을 만든 것
numbers += 5, 6,
print(numbers)

# 집합
# 특징: 순서가 정해져 있지 않고, 중복을 허용하지 않는다.
week = {"월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "월요일"}
print(week)

# 요소 추가
# add 가능한 요소 : 123, "문자", True, ("튜플")
# add 불가능한 요소 : [1, 2, 3], {keys:value}
week.add("화요일")
print(week)

# 0, 1이 요소로 들어가있는 경우 True, False는 중복으로 여겨 추가되지 않는다.
a = {0, "abc", 1}
a.add(True)
print(a)

# 튜플안에 있는 요소를 추가해주기
week.update(("일주일",))
print(week)

# 리스트와 딕셔너리에 있는 요소 추가하기
# 단, 딕셔너리는 key값만 요소로 들어간다.
week.update(["일주일"], {"한달": 123})
print(week)

# set 함수: 리스트를 집합으로 변환한다.
# 중복은 제거되고, 순서가 뒤바뀐다.
week = set(["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "금요일"])
print(week)

# 집합 연산
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# 합집합 : 중복을 제거하고 합쳐진다.
print(A | B)

# 교집합 : 중복된 값만 반환
print(A & B)

# 차집합 : A - B (A라는 집합에서 B라는 집합에 있는 원소를 뺀 집합)
print(A - B)

# 삭제
A.remove(4)
print(A)
